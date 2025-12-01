#1 Add 5 items to a list and remove the 3rd item.
l1=list(map(int,input("Enter 5 items").split(",")))
print("Original_list",l1)
#remove third item
l2=l1.pop(2)
print(l1)
print(l1[1])
#2 largest and smallest element
l1=list(map(int,input("Enter 5 items").split(",")))
lar=l1[0]
small=l1[0]
for i in l1:
    if i>lar:
        lar=i
for i in l1:
    if i<small:
        small=i
print("Largest:",lar)
print("Smallest:",small)
#3.Remove duplicate
l1=[1,33,33,44,55,66,55,22,33,45,44,2,2,2,2]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)



