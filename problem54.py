#program to search a item in a list using binary search
#assume list is sorted

def binary_search(list1, item,t):
    #this function returns true if item is in list1
    #takes list1 and item as arguments
    #t is index
    print("list is:",list1)
    print("item is:",item)
    print("t is:",t)
    #if list is empty return false
    #if list has only one element ,check if it is equal to item
    #if list has more than one element, check if middle element is equal to item or less than item or greater than item
    
    #case 1 list is singular
    if len(list1) == 1:
        if list1[0]==item:
            return True,t
        else:
            return False,-1                               #-1 means item not found
     
    #case 2 list is empty 
    elif len(list1) == 0:
        return False,-1
    
    #case 3 list has more than one element
    else:

        #3 cases again.if middle element is equal to item or less than item or greater than item
        if list1[int(len(list1)/2)]<item:
            return binary_search(list1[int(len(list1)/2)::],item,t+int(len(list1)/2))

        elif list1[int(len(list1)/2)]==item:
            return True,t+int(len(list1)/2)
        
        else:
            return binary_search(list1[:int(len(list1)/2):],item,t)


#generate a random list
#1 import library
import random


#2 generate list
l=[random.randint(-10,10) for i in range(10)]
l.sort()

print("list is:",l)
#3 generate item, which is to be searched
item=random.randint(-10,10)
print("Item to be searched:",item)
#search
a=binary_search(l,item,0)
print(a)



#4 check if answer is correct
print("Is answer correct?",a[0]==(item in l))



#5 print index by binary search and by index function
#item must be in list
if a[0]==True:
    print("Index by binary search:",a[1])
    print("Index by index function:",l.index(item))

