#Remove duplicates from List
l1=[1,2,3,4,4,5,6,7,7]
unique=[]
for i in l1:
	if i not in unique:
		unique.append(i)
print(unique)