#program to sort a list using quick sort technique

#define required function
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



#nwo check it for a  random list

import random 
l=[random.randint(-100,100) for i in range(10)]

print(l)
l1=list(l)
print(quick_sort(l1))
l.sort()
print(l)
