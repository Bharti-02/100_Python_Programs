def Even_odd(a):
    even=0
    odd=0
    for i in a:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
    
a=[1,2,3,4,5,6,7,8,9,11]
result=Even_odd(a)
print("Even:",result[0])
print("Odd:",result[1])



    
    