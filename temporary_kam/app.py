import json
train_data=[]
with open('gt.jsonl', 'r', encoding='utf-8') as f:
    data = json.loads(f)
    print(data)