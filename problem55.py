# Write a program which, given a text file comprising of all words in lower case, one word per line, sorts this file using bubble sort, merge sort and quick sort. Which technique is the fastest and why? Write a detailed report

#first define each alogorithmn in functions

#1; quick sort
def quick_sort(l):
    #This function will sort the list l using quick sort technique

    #as per algorithm , if list is empty or has only one element then it is already sorted
    if len(l)<2:
        return l
    else:
        #take pivot value as p
        p=l[-1]
        #remove p from list
        del l[-1]
        #create l1 for lower numbers and l2 for higher numbers
        l1=[]
        l2=[]
        for i in l:
            if i<p:
                l1.append(i)
            else:
                l2.append(i)
        #as per algorithm , return sorted before,p and then sorted after
        return quick_sort(l1)+[p]+quick_sort(l2)


#2; merge sort
def merge_sort(l):
    #this function takes a list as input and returns a sorted list using merge sort technique

    n=len(l)

    #first give ending of recursion
    if n<2:   #empty list of single element list
        return l

    else:
        #as per algorithm , divide the list into two parts and sort them
        l1=merge_sort(list(l[0:n//2:1]))
        l2=merge_sort(list(l[n//2::]))
        l3=[]
        #save required data in l3
        try:    #use try method in case one list is empty 
            #now as per algorithm , merge the two sorted lists
            while len(l1)!=0 and len(l2)!=0:
                if l1[0]<l2[0]:
                    l3.append(l1[0]);del l1[0]
                else:
                    l3.append(l2[0]);del l2[0]
        except IndexError:
            pass

        #if one list is empty ,then only will function come here.
        #one of them is empty so extend both as extending to empty list will not be a problem
        l3.extend(l1)
        l3.extend(l2)
        return l3

#3; bubble sort

#first define a function which iterate whole list once and swap two numbers if unordered and return new list and no of swaps
#the idea is to keep doing above untill no of swaps is zero

def round(l):
    swaps=0  #calculatinf the no of swaps
    for i in range(len(l)-1):     #-1 to avoid index error
        if l[i+1]<l[i]:  #if unordered then swap
            l[i],l[i+1]=l[i+1],l[i]
            swaps+=1
    return (l,swaps)


def bubble_sort(l):
    #this function sort the argument list using bubble sort technique
    swaps=1   #do start the loop

    #remember to call round function only once as that will be time consuming

    while swaps:      #if swaps is zero then its boolian value will be false and program will stop
        l,swaps=round(l)   #update llist and no of swaps at same time

    return l


#now to measure time taken by each algorithm, we will use time module
import time

#now calculate time taken by each algorithm
def time_taken(func):
    #this funciton measures time taken by function func to sort list l
    
    #import txt file and convert in to list
    a=open("ques55.txt","r").read()
    b=a.split("\n")
    #now b is the list
    #now calculate time taken by func to sort b

    start=time.time()
    func(b)
    end=time.time()

    return end-start



#first create a txt file with all words in lower case, one word per line
#we will use random module to generate random words
import random
a=open("ques55.txt","w")
for i in range(10**4):
    t=''
    for i in range(random.randint(1,10)):
        t+=chr(random.randint(97,123))
    a.write(t+"\n")
a.close()


#now save time taken in 3 variables x,y,z
x=time_taken(quick_sort)
y=time_taken(merge_sort)
z=time_taken(bubble_sort)

#x is supposed to be least and bubble sort is supposed to be most time consuming

#print absolute time taken by each algorithm
print("time taken by quick sort is",x)
print("time taken by merge sort is",y)
print("time taken by bubble sort is",z)

#print relative time taken by each algorithm
print("relative time taken by quick sort is",x/x)
print("relative time taken by merge sort is",y/x)
print("relative time taken by bubble sort is",z/x)


