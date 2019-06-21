""" Operators guide: 
    add = + 
    subtract = -
    multiply = *
    divide = /   """

num1 = float(input("Enter first number: "))  # float ensures the value entered is numeric!
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 + num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid Operator")