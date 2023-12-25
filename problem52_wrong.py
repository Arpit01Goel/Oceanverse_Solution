#program to sort list using merge sort

#defining required funciton
def merge_sort(l):
    n=len(l)   #length of list
    if n<2:
        return l
    elif n>=2:
        l1=list(l[0:n//2])
        l1.sort()
        l2=list(l[n//2::])
        l2.sort()
        l3=[]
        try :
            while len(l1)!=0 & len(l2)!=0:
                if l1[0]<l2[0]:
                    l3.append(l1[0])
                    del l1[0];print(len(l1))
                else:
                    l3.append(l2[0])
                    del l2[0];print(len(l2))
            if len(l1)==0 or len(l2)==0:
                l3.extend(l1);print(999)
                l3.extend(l2);print(888)
        except IndexError:
            l3.extend(l1)
            l3.extend(l2) 


        return l3

#now check if function is correct

#create random list
import random

l=[random.randint(0,100) for i in range(50)]
print(l)
l1=l.copy()
l1.sort()
print(l1)
L=merge_sort(l)
if L==l1:
    print("function is correct")
else:
    print("function is not correct")

print(L)


