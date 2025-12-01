#1.Print all numbers between 1 and 50 divisible by 3 and 5.
l1=[]
for i in range(1,51):
    if i%3==0 and i%5==0:
        l1.append(i)
print(l1)


#2.multiplication of table
num=int(input("Enter number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#3.Count how many even numbers exist in a list.
l1=[1,3,5,6,7,8,4,3,2]  
count=0
for i in l1:
    if i%2==0:
        count+=1
print("Even number:",count)
        
   