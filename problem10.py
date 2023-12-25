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

x=int(input("Enter the no"))
print(check_prime(x))
