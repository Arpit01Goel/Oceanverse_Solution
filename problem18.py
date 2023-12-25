a=0 #let us say sequence start from zero 
b=1
n=int(input("Enter the valuse of n")) # as per question take value of n
i=2
print(a,b,end=' ')
while i<n:
    a,b=b,a+b #defination of the fibonacci sequence
    print(b,end=' ') #printing next number
    i+=1 # taking next iteration or increment factor to terminate while loop when required
print() #to not alter the print position of termianl command prompt

