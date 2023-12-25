#to find factorial of a number using functions. 
#let us use recursion instead of looping

def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)

x=int(input("Enter the number"))
print(fact(x))



