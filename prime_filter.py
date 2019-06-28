""" This program filters out all prime numbers in a given range between
    between "a" and "b" inclusive """

a = int(input("Enter the first number in the range: "))
b = int(input("Enter the last number in the range: "))
updated_list = []

def prime_check(x):
    values = []
    for i in range(1, x+1):
        y = x/i
        values.append(y)

    integer_verifier = []

    for i in range(0, len(values)):
        z = values[i].is_integer()
        integer_verifier.append(z)

    true_counter = integer_verifier.count(True) 

    if true_counter == 2:
        updated_list.append(x)

def prime_filter(lower_bound,upper_bound):
    my_list = list(range(lower_bound, upper_bound+1))
    for i in range(0, upper_bound-lower_bound+1):
        prime_check(my_list[i])
    print(updated_list)

prime_filter(a, b)