""" This program can tell you whether a given integer is prime or not. 
    Simply run the code and enter the integer you want! """

x= int(input("Please enter an integer: "))
values = []

for i in range(1, x+1):
    y = x/i
    values.append(y)

integer_verifier = []

for i in range(0, len(values)):
    z = values[i].is_integer()
    integer_verifier.append(z)

true_counter = integer_verifier.count(True) 

if true_counter != 2:
    print("No", x, "is not a prime number.")
else:
    print("Yes", x, "is a prime number.")