#the smallest piece of line is a statement
# statements we know so far
# assignment statement:
i = 3
f = 3.4
msg = "hello"
message = 'hola' 
condition = True
# what does mean to assign something:
# asking to reseve memory of 4 bytes(this if the)
# and put the value 3 in it
# a variable is a memory that has a size,
# a name, an address, a value, and a type
# another statement is a function call
# the usage of a fuction is called a function call
# ex: print fuction call

print("hello world") # The fuction takes an argument 
#and print the value of it to the screem
print(3)
print(f)
print(condition)

print(i, type(i))
print(f, type(f))
print(msg, type(msg))
print(condition, type(condition))
# a function call has a name, and () and in between we have arugment
type(3)
input
# input wait for user input


# username = input("what is your name?") #This will evaluate to a text

# y = 3+4 #this evalutes to 7, so I evaluate the exp and put it in y

#print("welcome", username)

#Task: write a program that asks the user to input
#their name, and send a greeting massage with the name

Username = input ("what is your name?")
 
print("welcome", Username)

# what is casting funtion:
#inplict casting

x = 3
y =4
z = x//y # floor division(rounds to smaller number) 
# Ex:0.75 = 0
print("Value of z is", z, ". type of z is", type(z))
#0.75 = float
num = 14.5
age = int(num) # casting function 
print(age)
y = 4
yf = float(y)
print(yf)
text = str(y)
print(text)
#print(text + 7)Error

text_as_num = int(text)
print(text_as_num + 7) 

#a function does something, 
#but a function can also take input and output(doesnt have to but it can)
#input allways eval to a text or string

def printMessage():
    print("hello")

x= printMessage()
print(x)