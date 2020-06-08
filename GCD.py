# function to check the input
def check(p):
    q = None
    try:
        q = int(p)
    except ValueError:
        try:
            q = float(p)
            print("Please enter an integer")
            quit()
        except ValueError:
            print("You entered a character. Please enter an integer")
            quit()
    return(q)

# function to find divisors
def divisors(r):
    div = []
    for s in range(1,r+1):
        t = r % s
        if t == 0:
            div.append(s)
    return div

# function to find common divisors
def common_divisors(t,u):
    com_div = []
    for v in t:
        for w in u:
            if v == w:
                com_div.append(v)
    return com_div

# get input from user
a = input("Enter first number: ")
b = check(a)
c = input("Enter second number: ")
d = check(c)
if (b<=0 or d<=0):
    print('Please enter a positive integer')
else:
    # call divisors finding function
    div_b = divisors(b)
    div_d = divisors(d)
    print('The divisors of your first number are', div_b)
    print('The divisors of your second number are', div_d)

    # call common divisors finding function
    c_div = common_divisors(div_b,div_d)

    # print GCD
    print("The GCD of your numbers is",max(c_div))
