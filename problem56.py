#Write a program to find the median element in a list of unsorted elements. You are not supposed to sort the list


""" Given any list.
We will take any random element and put smaller elements on left and larger elements on right.
Although median is required, we will find any element at position y as it is difficult but taught.
"""


import random


def search(l,y):
    #This funciton will return the yth smallest element in the list l
    

    #calculate the no of elements in list to reduce the time complexity by not calculating it again and again
    n=len(l)
    
    #special cases
    if n==0:
        return None
    if n==1:
        return l[0]

    #select any random element
    r=l[random.randint(0,n-1)]


    #divide the list into two parts plus the random element
    l1=[]
    l2=[]
    l3=[]

    #append elements in proper list
    for i in l:
        if i<r:
            l1.append(i)
        elif i==r:
            l2.append(i)
        else:
            l3.append(i)
    
    #store the no of elements in each list to reduce the time complexity by not calculating it again and again
    t1=len(l1)
    t2=len(l2)
    t3=len(l3)
    
    
    #see the list divided into three parts :elements below r, elements equal to r and elements above r
    #required element must be in one of the three parts
    #check each part one by one

    if t1<y:        #required element is in the right part or middle part
        if y<t1+t2+1:  #required element is the random element
            return r
        else:          #required element is in the right most part
            return search(l3,y-(t1+t2))
    else:               #required element is in the left part
        return search(l1,y)

"""
#take input from user the no of elements in list
n=int(input("Enter the no of elements in list: "))

#generate a list of n random elements ( all integers between -100 and 100)
list1=[random.randint(-10**3,10**3) for i in range(n)]

#take input from user the position of element to be found
y=int(input("Enter the position of element to be found: "))

#store the element found in a.we will check our answer later
a=search(list1,y)

list1.sort()

#check if the element found is correct or not
if a==list1[y-1]:
    print("The element found is correct")
else:
    print("The element found is incorrect")

print("The element found is: ",a)
"""

#now to solve the question we will take input the list size ( no of elements in list) and then find the median element\

#but the problem comes when we have even no of elements in list
#we will take the average of two middle elements as median

#take input from user the no of elements in list
t=int(input("Enter the no of elements in list: "))

#generate a list of n random elements ( all integers between -10**6 and 10**6)
list1=[random.randint(-10**4,10**4) for i in range(t)]    #take smaller range so that elements can repeat


#two cases arise: 1; n is odd 2; n is even
#odd is easy 

if t%2==1:
    print("The median element is: ",search(list1,int(((t+1)/2))))
else:
    print("The median element is: ",(search(list1,int(t/2))+search(list1,int(t/2)+1))/2)

