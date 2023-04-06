import json
with open('gt.jsonl','r') as json_file:
    data = json.load(json_file)
print(data)
for elem in range(len(data['html']['cells'])):
    bbox = data['html']['cells'][elem]['bbox']

    sing = list()
    for two in bbox:
        sing.append(two[0])
        sing.append(two[1])
    data['html']['cells'][elem]['bbox'] = sing

with open ('writeme.txt', 'w') as json_file:  
    json.dump(data, json_file)
    