#Write a program to find the median element in a list of unsorted elements. You are not supposed to sort the list

#we will define a funciton which will take a list as an argument and return the median of the list


#we will also need to define a function which will take a item and list as argument and return how many elements are less than , grater than and equal to the item

def data(item,l):
    less=0
    equal=0

    for i in l:
        if i<item:
            less+=1
        elif i==item:
            equal+=1
    return [less,equal,len(l)-less-equal]
        
def check_median(item,l):
    #l has data of the item (less,equal,greater)

    a=((greater-less)**2)**(0.5)
    b=equal%2


def median(l):
    #This will return the median of the list
    
    n=len(l)
    if n%2!=0:
        #if the length of the list is odd
        #then the median will be the middle element
        for i in l:
            [a,b,c]=data(i,l)
            if (((a-c)**2)**(0.5))-(b%)==0:
                return i
    else:
        #if the length of the list is even
        




l=eval(input("Enter the list: "))
print("The median of the list is: ",median(l))
