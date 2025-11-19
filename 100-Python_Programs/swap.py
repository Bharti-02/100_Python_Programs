# Function to swap two numbers
def swap(a, b):
    a, b = b, a
    return a, b

# Input
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

print("Before swap: a =", a,",b =", b)

# Calling function
a, b = swap(a, b)

print("After swap: a =", a, ", b =", b)

