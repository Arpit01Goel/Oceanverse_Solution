#Program to calculate simple interest
#Take input of principal, rate and time from user
#Calculate simple interest and print it


prin=int(input("Enter principal"))
rate=float(input("Enter rate percentage"))
time=int(input("Enter years"))
#simple interest formula is prin*rate*time/100
print(f"calculated interest is {prin*rate*time/100}")
