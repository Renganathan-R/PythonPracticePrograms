# function generating Fibonacci sequence and returning nth Fibonacci number
def fibonacci(c):
    fib=[0,1]
    d=fib[0]
    e=fib[1]
    for f in range(1,c):
        g=d+e
        fib.append(g)
        d=fib[f]
        e=fib[f+1]
    return fib[-1]

# get input from user
a = input("Enter an integer: ")
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

# calculate and print the nth Fibonacci number
if b<0:
    print("please enter zero or a positive integer")
elif b==0:
    print('Your fibonacci number is',b)
elif b==1:
    print('Your fibonacci number is',b)
else:
    print('Your fibonacci number is', fibonacci(b))
