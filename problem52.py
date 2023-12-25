#Write a program to sort a list of numbers using the merge sort technique

#defining the required function
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

#generate random list
import random
l=[random.randint(-100,100) for i in range(20)]
#print list

print(l)
#now sort using merge sort
print(merge_sort(l))
#sort using in build method to check answer
l.sort()
print(l)
