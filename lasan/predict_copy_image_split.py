import pandas as pd
import numpy as np
import pytesseract
import torch
import os
import json
from PIL import Image, ImageDraw, ImageFont
from transformers import LayoutLMv2Processor
import warnings
from appconfig import AppConfig
from flask import session
import re
from collections import defaultdict

warnings.filterwarnings('ignore')
#pytesseract.pytesseract.tesseract_cmd = AppConfig.TESSERACT
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
 
def random_color():
    return np.random.randint(0,255,3)

def normalize_box(bbox,width,height):
  return [
          int(bbox[0]*(1000/width)),
          int(bbox[1]*(1000/height)),
          int(bbox[2]*(1000/width)),
          int(bbox[3]*(1000/height)),
  ]

def compare_boxes(b1,b2):
  b1 = np.array([c for c in b1])
  b2 = np.array([c for c in b2])
  equal = np.array_equal(b1,b2)
  return equal

def mergable(w1,w2):
  if w1['label'] == w2['label']:
    threshold = 7
    if abs(w1['box'][1] - w2['box'][1]) < threshold or abs(w1['box'][-1] - w2['box'][-1]) < threshold:
      return True
    return False
  return False

# Display extracted data to text box 
def process_text(dictionary):

    labels = defaultdict(lambda : [None,0])
    for i in dictionary['form']:
        if i['label']!='OTHER' and ((labels[i['label']][0] is None) or labels[i['label']][1]<=len(i['words'])):
            labels[i['label']][0] = i['text']
            labels[i['label']][1] = len(i['words'])
    labels_processed = defaultdict(lambda : None)
    for i in labels:
        if i=='COMP_NAME' or i=='COMP_ADD' or i=='INVOICE_NO' or i=='INVOICE_DATE' or i=='DELIVERY_NOTE' or i=='DELIVERY_DATE':
            labels_processed[i] = re.sub('[^a-zA-Z0-9./&\- ]','',labels[i][0])
        elif i == 'COMP_CIN' or i=='COMP_GST':
            labels_processed[i] = re.sub('[^0-9A-Za-z ]','',labels[i][0])
        elif i == 'COMP_STATE' :
            labels_processed[i] = re.sub('[^A-Za-z ]','',labels[i][0])
        elif i == 'COMP_STATE_CODE':
            labels_processed[i] = re.sub('[^0-9 ]','',labels[i][0])
        elif i == 'TOTAL' or i == 'TAXABLE_VALUE' or i == 'TAX_AMOUNT':
            labels_processed[i] = re.sub('[^a-zA-Z0-9,. ]','',labels[i][0])

    return labels_processed

class Model:
    def __init__(self, session):
        self.model = torch.load(AppConfig.MODEL_PATH, map_location = DEVICE)
        self.session = session
        self.inference_processor = LayoutLMv2Processor.from_pretrained("./bigscience_t0", revision="no_ocr")
    def get_image(self, image_path):
        self.inference_image = Image.open(os.path.join(self.session['UPLOAD'],image_path)).convert('RGB')
        self.width, self.height = self.inference_image.size
        
    def image_to_data(self,image_path):
        self.get_image(image_path)
        data = pytesseract.image_to_data(os.path.join(session['UPLOAD'],image_path));
        with open(os.path.join(session['OUTPUT'],image_path[:-4]+'.tsv'),'w') as f:
            f.write(data)
        ocr_df = pd.read_csv(os.path.join(session['OUTPUT'],image_path[:-4]+'.tsv'),encoding= 'unicode_escape', sep='\t', engine='python', error_bad_lines=False)
        os.remove(os.path.join(session['OUTPUT'],image_path[:-4]+'.tsv'))
        ocr_df = ocr_df.dropna()
        ocr_df = ocr_df.drop(ocr_df[ocr_df.text.str.strip() == ''].index)
        text_output = ocr_df.text.tolist()
        self.doc_text = ' '.join(text_output)
        self.words = []
        for index,row in ocr_df.iterrows():
            word = {}
            origin_box = [row['left'],row['top'],row['left']+row['width'],row['top']+row['height']] 
            word['word_text'] = row['text']
            word['word_box'] = origin_box
            word['normalized_box'] = normalize_box(word['word_box'],self.width, self.height)
            self.words.append(word)
        self.boxlist = [word['normalized_box'] for word in self.words]
        self.wordlist = [word['word_text'] for word in self.words]
        
    def predict(self,image_path):
        self.image_to_data(image_path)
        self.encoding = self.inference_processor(self.inference_image,
                                            self.wordlist,
                                            boxes=self.boxlist,
                                            return_tensors="pt",
                                            padding="max_length", 
                                            truncation=True) 
        for k,v in self.encoding.items():
            self.encoding[k] = v.to(DEVICE)
        self.model.eval()
        with torch.no_grad():
            self.outputs = self.model(**self.encoding)
        
    def decode(self,image_path, saving_name):
        raw_input_ids = self.encoding['input_ids'][0].tolist()
        predictions = self.outputs.logits.argmax(-1).squeeze().tolist()
        token_boxes = self.encoding.bbox.squeeze().tolist()
        special_tokens = [self.inference_processor.tokenizer.cls_token_id, 
                          self.inference_processor.tokenizer.sep_token_id,
                          self.inference_processor.tokenizer.pad_token_id]

        input_ids = [id for id in raw_input_ids if id not in special_tokens]
        predictions = [self.model.config.id2label[prediction] for i,prediction in enumerate(predictions) if not (raw_input_ids[i] in special_tokens)]
        actual_boxes = [box for i,box in enumerate(token_boxes) if not (raw_input_ids[i] in special_tokens )]

        assert(len(actual_boxes) == len(predictions))
        
        for word in self.words:
            word_labels = [] 
            token_labels = []
            word_tagging = None 
            for i,box in enumerate(actual_boxes,start=0):
                if compare_boxes(word['normalized_box'],box):
                    if predictions[i] != 'O':
                        word_labels.append(predictions[i][2:])
                    else:
                        word_labels.append('O')
                token_labels.append(predictions[i])
            if word_labels != []:
                word_tagging =  word_labels[0] if word_labels[0] != 'O' else word_labels[-1]
            else:
                word_tagging = 'O'
            word['word_labels'] = token_labels
            word['word_tagging'] = word_tagging
            
        filtered_words = [{'id':i,'text':word['word_text'],
                            'label':word['word_tagging'],
                            'box':word['word_box'],
                            'words':[{'box':word['word_box'],
                            'text':word['word_text']}]} for i,word in enumerate(self.words) if word['word_tagging'] != 'O']

        
        merged_taggings = []
        for i,curr_word in enumerate(filtered_words):
            skip = False
            neighbors = lambda word:[neighbor for neighbor in filtered_words if mergable(word,neighbor)]
            for items in merged_taggings:
                for item in items:
                    if item in neighbors(curr_word):
                        skip = True
                        break
                if skip:
                    break
            if skip:
                continue
            merged_taggings.append(neighbors(curr_word))

        merged_words = []
        for i,merged_tagging in enumerate(merged_taggings):
            if len(merged_tagging) > 1:
                new_word = {}
                merging_word = " ".join([word['text'] for word in merged_tagging])
                merging_box = [merged_tagging[0]['box'][0]-5,merged_tagging[0]['box'][1]-10,merged_tagging[-1]['box'][2]+5,merged_tagging[-1]['box'][3]+10]
                new_word['text'] = merging_word
                new_word['box'] = merging_box
                new_word['label'] = merged_tagging[0]['label']
                new_word['id'] = filtered_words[-1]['id']+i+1
                new_word['words'] = [{'box':word['box'],'text':word['text']} for word in merged_tagging]
                merged_words.append(new_word)

        filtered_words.extend(merged_words)
        predictions = [word['label'] for word in filtered_words]
        actual_boxes = [word['box'] for word in filtered_words]
        unique_taggings = set(predictions)
        label2color = {f'{label}':f'rgb({random_color()[0]},{random_color()[1]},{random_color()[2]})' for label in unique_taggings}
        
        inference_image = Image.open(os.path.join(session['UPLOAD'],saving_name)).convert('RGB')
        draw = ImageDraw.Draw(inference_image)
        font = ImageFont.load_default()
        # taggings = {}
        for prediction, box in zip(predictions, actual_boxes):
            if prediction!='OTHERS':
                draw.rectangle(box, outline=label2color[prediction])
                draw.text((box[0] + 10, box[1] - 10), text=prediction, width=50, fill=label2color[prediction], font=font)  

        doc_name = os.path.basename(session['UPLOAD'])
        os.makedirs(session['OUTPUT'],exist_ok=True)
        inference_image.save(f"{session['OUTPUT']}/{saving_name}")
        dictionary = {"document name":doc_name,"document": self.doc_text , "form": filtered_words}
        with open(f"{session['OUTPUT']}/{saving_name[:-4]}.json","w",encoding='utf8') as outfile:
            di=  {}
            di['INVOICE_NO']      = 'None'
            di['INVOICE_DATE']    = 'None'
            di['DELIVERY_NOTE']   = 'None'
            di['DELIVERY_DATE']   = 'None'
            di['COMP_NAME']       = 'None'
            di['COMP_ADD']        = 'None'
            di['COMP_CIN']        = 'None'
            di['COMP_GST']        = 'None'
            di['COMP_STATE']      = 'None'
            di['COMP_STATE_CODE'] = 'None'
            di['TOTAL']           = 'None'
            di['TAXABLE_VALUE']   = 'None'
            di['TAX_AMOUNT']      = 'None'
            # print(process_text(dictionary))
            # di.update(json.loads(json.dumps(process_text(dictionary))))
            di.update(process_text(dictionary))
            print(di)
            json.dump(di,outfile)
        # print(di)
        # json.dump(di, outfile, ensure_ascii=False)
        # return di , inference_image