a = input("enter first number: ")
b = input("enter second number: ")
c = input("enter third number: ")
max = 0
if a > b:
    max = a 
else:
    max = b
if c > max:
    max = c
print("Maximum is", max)