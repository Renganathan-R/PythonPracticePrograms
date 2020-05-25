# function to find the factorial
def factorial(c):
    d = 1
    if c==0:
        return 1
    else:
        while(c>0):
            d = d*c
            c = c-1
        return d

# get input from user
a = input("Enter a integer: ")
b = None

# check the type of input
try:
    b = int(a)
except ValueError:
    try:
        b = float(a)
        print("Please enter an integer")
        quit()
    except ValueError:
        print("You entered a character. Please enter an integer")
        quit()
# calculate and print the factorial
if b<0:
    print("please enter zero or a positive integer")
else:
    print("The factorial of your number is", factorial(b))
