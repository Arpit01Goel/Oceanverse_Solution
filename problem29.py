#29. Decimal to Binary Conversion: Write a program that converts a decimal number to its binary representation using loops, without using built-in conversion functions.
#
def f(x):
    if x==0:
        return 0
    else:
        return 1
#defining a function to calculate binary    
def bi(x,y,i):
    if x==0:
        if y=='':        #condition for no is 0
            return 0  
        else:    #no already converted to its binary
            return y
    else:
        return bi(x-(x%(2**i)),str(f(x%(2**i)))+y,i+1)    #taking ramainder when dividing by powers of 2. but if remainder is 2, we just have to take 1 so f(x) is required.Its one of method to convert to binary . 

while 1:
    #Taking input of no and printing its binary
    print(bi(int(input()),'',1))

