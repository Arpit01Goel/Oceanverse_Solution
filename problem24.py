#Define a function that conveert celcius to farenheit
#Define a function that conveert farenheit to celcius
#Ask user to input mode
#Ask user to input numerical value
#Print the result

def c_f(c):
    f=c*(9/5)+32    #apply formula for coversion
    return f
def f_c(f):
    c=(f-32)*5/9    #apply formula for conversion
    return c
i=input("Enter mode: \nc to f :0 \nf to c:1 \n")    #choose mode, which to which
x=float(input("Enter numerical value"))
if i=='0': # implying mode
    print(c_f(x))
else:
    print(f_c(x))

