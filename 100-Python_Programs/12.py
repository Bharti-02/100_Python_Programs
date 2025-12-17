# search element
'''l1=[2,3,4,6,7,8,9,10]
target=int(input("Enter number what you want to search"))
if target in l1:
    print("Found")
else:
    print("Not found")'''
    
# count greater number 

'''l1=[2,3,4,5,6,7,8,9]
target=3
count=0
for i in range(len(l1)):
    if l1[i] > target:
        count+=1

print(count)'''

# less than and equal to 
'''l1=[2,3,4,5,6,7,8,9]
target=3
count=0
for i in l1:
    if i <= target:
        count+=1
print(count)'''

# even and greater than
l1=[2,3,4,5,6,7,8,9,87,65]
target=2
count=0
for i in l1:
    if i > target and i%2==0:
        count+=1

print(count)



