#defining function to find both gcd and no of iterations
def gcd(a,b,i):
    if a<b:     #just in case order mess up
        return gcd(b,a,i)
    elif a%b==0:
        return (b,i)      #thats how algorithm works
    else:
        return gcd(b,a%b,i+1)

#also calculate execution time
import time
#take value from user as specified
k=int(input("Enter the value of k"))
init=time.time()

#define variable to store so important data
itr=0
a=0
b=0
max_itr=0
final_list=[]
#list will contain all possible pairs in case multiple answers exists

for i in range(10**(k-1),10**k):
    for j in range(10**(k-1),i+1):     #reduce calculating a pair twice
        itr=gcd(i,j,0)[-1]
        if itr>max_itr:
            final_list=[(i,j,itr)]
            max_itr=itr
        #also accout for multiple answers
        elif itr==max_itr:
            final_list.append((i,j,itr))
#print required answer and time taken
print(final_list)
final=time.time()
print(final-init)
