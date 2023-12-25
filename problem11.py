#defining a function to check prime number
def check_prime(x):
    if x==2:
        return True
    elif x<2 or x%2==0:
        return False
    else:
        for i in range(3,int(x**(0.5))+1,2):
            if x%i==0:
                return False
        else:
            return True

n=int(input("Enter the n"))
#for every number below n+1 and above 1 , check if it is prime. If it is , print it.
for i in range(2,n+1):
    if check_prime(i):
        print(i)
