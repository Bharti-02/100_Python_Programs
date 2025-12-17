#largest number 
l1=[2,3,4,5,66,77,88,55,432,45]
lar=l1[0]
for i in l1:
    if i > lar:
        lar=i 

print("Largest number",lar)

# second largest  number 
l1=[2,3,4,5,66,77,88,55,432,45]
largest=l1[0]
second_largest=l1[0]

for i in l1:
    if i > largest:
        second_largest=largest
        largest=i 
    elif i > second_largest and i != largest:
        second_largest=i 

print("Second_Largest",second_largest)
        
    
        