
import json
import os

studentsList = []

with open('train.txt') as f:
    for jsonObj in f:
        studentDict = json.loads(jsonObj)
        studentsList.append(studentDict)

with open('train_output.json','w') as json_file:
    json.dump(studentsList, json_file)

with open('train_output.json','r') as json_file:
    data = json.load(json_file)

# print(data)
for temp in data:
    if 'gt' in temp.keys():
        del temp['gt']

final_list = list()
for one_dictionary in data:
    print(one_dictionary)
    for elem in range(len(one_dictionary['html']['cells'])):
        bbox = one_dictionary['html']['cells'][elem]['bbox']

        sing = list()
        for two in bbox:
            sing.append(two[0])
            sing.append(two[1])
        one_dictionary['html']['cells'][elem]['bbox'] = sing

    final_list.append(one_dictionary)

with open ('writeme.json', 'w') as json_file:  
    json.dump(final_list, json_file)


with open('writeme.json','r') as json_file:
    data = json.load(json_file)

for ekle in data:
    with open("student.txt", "a") as write_file:   
            write_file.write(str(ekle))
            write_file.write('\n')

fin = open("student.txt", "rt")

fout = open("out.txt", "wt")

for line in fin:
	
	fout.write(line.replace("'", "\""))

fin.close()
fout.close()
os.remove('writeme.json')
os.remove('train_output.json')
os.remove('student.txt')
