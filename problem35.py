#program to define a fuction which take n as input and print nth term of fibonacci series

def fib(n):
    if n in {0,1,2}:
        return [0,1,1][n]
    else:
        a,b=0,1
        i=2
        while i<n:
            a,b=b,a+b
            i+=1
        return b
n=int(input("Enter the number of term: "))
print(fib(n))

