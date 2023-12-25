#program to create n identical bins and throw balls in them untill all are non empty.

import random
def throw_balls(n):

    #create a box
    box={}

    #create empty bins
    for i in range(1,n+1):
        box[i]=0
    #we will count no of balls. So define a variable no_of_balls for it and increase it everytime ball is thrown
    no_of_balls=0
    #throw balls in bins
    while 0 in box.values():
        box[random.randint(1,n)]+=1
        no_of_balls+=1

    #experiment completed
    #return no of balls as asked 
    print(f"No of balls thrown: {no_of_balls}")
    
     
#take n as input from user

n=int(input("Enter no of bins: "))

#Do simulation
throw_balls(n)

