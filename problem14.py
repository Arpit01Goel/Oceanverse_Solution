n1=input("Enter string")
n2=''
#saving reverse of string in n2
for i in range(1,len(n1)+1):
    n2+=n1[-i]
print(n2)

