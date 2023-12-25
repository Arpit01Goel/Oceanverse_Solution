#program to solve the contiguous sum sub array problem

def max_sum(x):
    #This function takes input a list and returns the maximum sum of a contiguous sub array,i.e., the maximun sum of a continuous sub list

    max=0
    i=0
    for j in range(len(n)):
        i+=n[j]
        if i>max:
            max=i
        if i<0:
            i=0
    return max

#test it for a random list
#import random library
import random

#generate a random list of random numbers

n=[random.randint(-100,100) for i in range(random.randint(0,10))]

#print required data
print("The list is: ",n)
print("The maximum sum is: ",max_sum(n))

