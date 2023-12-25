#26. Divisible by 7 and 5: Write a program that checks if a number provided by the user is divisible by both 7 and 5. Generalize it to a and b.



a,b=int(input("Enter a")),int(input("Enter b")) #take values of a nad b as input
x=int(input("Enter no")) #take value of x
if x%a==0 and x%b==0:  #check if divisible by both
    print("yes") 
else:
    print("no")
