#defining a function named is_even which return weather no is even or not for any integer.

def is_even(x):
    return bool(not x%2)
while 1:
    print(is_even(int(input())))
