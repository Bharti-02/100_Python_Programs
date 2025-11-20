#check number is odd and even
def Odd_Even(num):
	if num % 2==0:
		print(f"{num}:Even")

	else:
		print(f"{num}:Odd")
num=int(input("Enter number:"))
Odd_Even(num)
