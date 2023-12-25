#Write a program to sort a list of numbers using the bubble sort technique


#first define a function which iterate whole list once and swap two numbers if unordered and return new list and no of swaps
#the idea is to keep doing above untill no of swaps is zero

def round(l):
    swaps=0  #calculatinf the no of swaps
    for i in range(len(l)-1):     #-1 to avoid index error
        if l[i+1]<l[i]:  #if unordered then swap
            l[i],l[i+1]=l[i+1],l[i]
            swaps+=1
    return (l,swaps)


#defining the requiered funciton
def bubble_sort(l):
    #this function sort the argument list using bubble sort technique
    swaps=1   #do start the loop

    #remember to call round function only once as that will be time consuming

    while swaps:      #if swaps is zero then its boolian value will be false and program will stop
        l,swaps=round(l)   #update llist and no of swaps at same time 

    return l

#calculate time taken by the function and compare with in build function

#first create a list of random numbers
import random
l=[random.randint(1,100) for i in range(10000)]
print(l)
#.sort() function is inplace function so we have to create a new list
l1=l.copy()

import time 

#time taken by in build function
initial=time.time()
l1.sort()
final=time.time()
build_time=final-initial
#time taken by our function
#print(l)
initial=time.time()
bubble_sort(l)
final=time.time()
our_time=final-initial

#check if funciton is correct
print(l1==l)

#print comparision
print("Time taken by in build function is ",build_time)
print("Time taken by our function is ",our_time)
print("Efficiency of our funciton is :",build_time/our_time)
#print("all the lists are:")
#print(f"in build function list: {l1} \nour function list: {l}")
