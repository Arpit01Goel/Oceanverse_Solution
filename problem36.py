#program to simulate throwing n balls in n bins using function

#importing required modules
import random


def throw_balls(n):

    #create n bins
    box={}
    for i in range(1,n+1):
        box[i]=0

    #throwing n balls randomly (as all bins are identical, equilly probible)
    for i in range(n):
        box[random.randint(1,n)]+=1
    max=0
    for i in box:
        if box[i]>max:
            max=box[i]
    return max

#now smulation of experiment saved in a function.
#collecting data

for i in range(1,10):
    n=10**i
    max_ball_average=0
    for i in range(100):
        max_ball_average+=throw_balls(n)
    max_ball_average/=100
    print("for n=",n,"average max ball in a bin is",max_ball_average)
    

