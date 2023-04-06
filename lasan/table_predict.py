import os
from mmdet.apis import init_detector, inference_detector
from PIL import Image
import cv2
import numpy as np
import pandas as pd
from paddleocr import PaddleOCR
import tensorflow as tf
from preprocess_csv_file import preprocess_csv_file
ocr = PaddleOCR(lang='en', det_db_score_mode='slow',use_dilation=True, show_log=False)

class PredictFunc():
    def __init__(self,file_name,session):

        self.file_name = file_name
        self.image_path= os.path.join(session['UPLOAD'], file_name)
        self.checkpoint_file = 'description.pth'
        self.config_file = 'default_runtime.py'
        self.device='cpu'
        self.model = init_detector(self.config_file, self.checkpoint_file, device=self.device)
        self.session = session
    
        result = inference_detector(self.model, self.image_path)
        x,y,w,h,s = result[0][0]
        session['x'],session['y'],session['w'],session['h'] = int(x),int(y),int(w),int(h)
        img = Image.open(self.image_path)
        img2 = img.crop((x,y,w,h))
        # print(self.image_path)
        # print('-------------------------------------------------')
        self.image_path = os.path.join(session['SAMPLE_IMAGE'],file_name)
        img2.save(self.image_path)
        
        image_cv = cv2.imread(self.image_path)
        image_height = image_cv.shape[0]
        image_width = image_cv.shape[1]
        output = ocr.ocr(self.image_path, cls=False)
        
        boxes = [line[0] for line in output]
        texts = [line[1][0] for line in output]
        probabilities = [line[1][1] for line in output]
        image_boxes = image_cv.copy()
        for box,text in zip(boxes,texts):
          cv2.rectangle(image_boxes, (int(box[0][0]),int(box[0][1])), (int(box[2][0]),int(box[2][1])),(0,0,255),1)
          cv2.putText(image_boxes, text,(int(box[0][0]),int(box[0][1])),cv2.FONT_HERSHEY_SIMPLEX,1,(222,0,0),1)
        im = cv2.imread(self.image_path,0)
        os.remove(self.image_path)
        horiz_boxes = []
        vert_boxes = []
        for box in boxes:
          x_h, x_v = 0,int(box[0][0])
          y_h, y_v = int(box[0][1]),0
          width_h,width_v = image_width, int(box[2][0]-box[0][0])
          height_h,height_v = int(box[2][1]-box[0][1]),image_height
          horiz_boxes.append([x_h,y_h,x_h+width_h,y_h+height_h])
          vert_boxes.append([x_v,y_v,x_v+width_v,y_v+height_v])
          cv2.rectangle(im,(x_h,y_h), (x_h+width_h,y_h+height_h),(0,0,255),1)
          cv2.rectangle(im,(x_v,y_v), (x_v+width_v,y_v+height_v),(0,255,0),1)
        horiz_out = tf.image.non_max_suppression(
            horiz_boxes,
            probabilities,
            max_output_size = 1000,
            iou_threshold=0.1,
            score_threshold=float('-inf'),
            name=None
        )
        horiz_lines = np.sort(np.array(horiz_out))
        im_nms = image_cv.copy()
        for val in horiz_lines:
          cv2.rectangle(im_nms, (int(horiz_boxes[val][0]),int(horiz_boxes[val][1])), (int(horiz_boxes[val][2]),int(horiz_boxes[val][3])),(0,0,255),1)
        vert_out = tf.image.non_max_suppression(
            vert_boxes,
            probabilities,
            max_output_size = 1000,
            iou_threshold=0.1,
            score_threshold=float('-inf'),
            name=None
        )
        vert_lines = np.sort(np.array(vert_out))
        for val in vert_lines:
          cv2.rectangle(im_nms, (int(vert_boxes[val][0]),int(vert_boxes[val][1])), (int(vert_boxes[val][2]),int(vert_boxes[val][3])),(255,0,0),1)
        out_array = [["" for i in range(len(vert_lines))] for j in range(len(horiz_lines))]
        unordered_boxes = []
        for i in vert_lines:
          unordered_boxes.append(vert_boxes[i][0])
        ordered_boxes = np.argsort(unordered_boxes)
        def intersection(box_1, box_2):
          return [box_2[0], box_1[1],box_2[2], box_1[3]]
        def iou(box_1, box_2):
          x_1 = max(box_1[0], box_2[0])
          y_1 = max(box_1[1], box_2[1])
          x_2 = min(box_1[2], box_2[2])
          y_2 = min(box_1[3], box_2[3])
          inter = abs(max((x_2 - x_1, 0)) * max((y_2 - y_1), 0))
          if inter == 0:
              return 0   
          box_1_area = abs((box_1[2] - box_1[0]) * (box_1[3] - box_1[1]))
          box_2_area = abs((box_2[2] - box_2[0]) * (box_2[3] - box_2[1]))
          return inter / float(box_1_area + box_2_area - inter)
        for i in range(len(horiz_lines)):
          for j in range(len(vert_lines)):
            resultant = intersection(horiz_boxes[horiz_lines[i]], vert_boxes[vert_lines[ordered_boxes[j]]] )
            for b in range(len(boxes)):
              the_box = [boxes[b][0][0],boxes[b][0][1],boxes[b][2][0],boxes[b][2][1]]
              if(iou(resultant,the_box)>0.1):
                out_array[i][j] = texts[b]
        out_array=np.array(out_array)
        data = pd.DataFrame(out_array)
        # print(data)
        data = data.style.set_properties(**{'text-align': 'left'})
        # data.to_excel(os.path.join(session['SAMPLE_IMAGE'],file_name.split('.')[0]+'.xlsx'), index=False)
        # df_1 = preprocess_csv_file(file_name ,session['SAMPLE_IMAGE'], session['id'])
        data.to_excel(os.path.join(session['SAMPLE_IMAGE'],file_name.split('.')[0]+'.xlsx'), index = None, header=False)


