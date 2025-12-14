#second largest element
a=[20,34,54,65,67,89]
max1 = a[0]
max2 = a[0]
for i in a:
    if i > max1:
        max2=max1
        max1=i 
    elif i> max2 and i != max1:
        max2=i    
print(max2)