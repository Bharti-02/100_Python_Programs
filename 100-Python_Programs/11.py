#sorted
def sort_arr(a):
    for i in range(len(a) -1):
        if a[i]>a[i+1]:
            return False
        
    return True
a=[10,20,30,40,50,60]
result=sort_arr(a)
print(result)