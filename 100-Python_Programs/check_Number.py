#Solution1
#Positive Negative and Zero
'''a=int(input("Enter number:"))
if a > 1:
	print("Positive number")
elif a<1:
	print("Negative number")
else:
	print("Zero")'''

#Solution 2
def check_Number(a):

	if a==0:
		print("Zero")
	elif a<1:
		print("Negative")
	else:
		print("Positive")

a=int(input("Enter number:"))
check_Number(a)