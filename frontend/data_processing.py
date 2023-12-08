import csv
import math
data_list=[]
with open('data/data_dummy.csv') as csvfile:
	data=csv.reader(csvfile)
	for row in data:
		if row[0]!='Classroom' and row[1]!='Students' and row[2]!='Exit time' and row[3]!='Status':
			classno=row[0]
			students=row[1]
			exit_time=row[2]
			status=row[3]
			# print(f'{classno} {students} {exit_time} {status}')
			data_list.append([classno,students,exit_time,status])
# count=0
# for i in range(len(data_list)):
# 	if data_list[i][0]=="1201":
# 		count+=1
class_count_percentage=[]
classnos=[item[0] for item in data_list]
classes=sorted(set(classnos))
classes.remove('')
classes=list(classes)
# print(classes)

for i in classes:
	count=classnos.count(i)
	per=round((count/80),1)*100
	class_count_percentage.append([i,count,per])

print(class_count_percentage)
# for i in range(len(data_list)):
# 	classno=data_list[i][0]
# print(data_list[0][0])