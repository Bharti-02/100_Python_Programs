# count vowels 
l1=['a','b','c','d','a','e','o']
vowels=['a','e','i','o','u']
count=0
for i in l1:
    if i in vowels:
        count+=1
print(count)
# largest number
l1=[1,44,66,77,12,32]
lar=l1[0]
for i in l1:
    if i >lar:
        lar=i
print("Largest:",lar)
# return even number from a list
l1=[1,3,4,5,6,7,211,22,44]
even_number=[]
for i in l1:
    if i %2==0:
        even_number.append(i)  
print(even_number) 
#palindrome
a=input("Enter:")
pali=a[::-1]
if a==pali:
    print("Palindrome")
else:
    print("Not Palindrome")
# 
num=[]
for i in range(1,51):
    if i % 7 !=0:
        num.append(i) 
print(num)