#Take input of year from user and print whether it is leap year or not.

x=int(input("Enter the value of year"))
#A year is leap if it is divisible by 4 but if it is divisible by 100 it will not be. The last rule is if it is multiple of 400 , it surely will be.
if x%400==0 or (x%4==0 and x%100!=0):
    print("Leap")
else:
    print("not leap")
