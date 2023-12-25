#Take input both lists of lists

a=eval(input("Enter the first list of lists: "))
b=eval(input("Enter the second list of lists: "))

#now to calculate sum first create a list of same structure
#remember c=a will be tragidy in python ( c will refer to a then. any change in c will also change a and vice versa.
c=list(a)

#now to calculate sum of elements of both lists
for i in range(len(c)):  #i gives the number of rows
    for j in range(len(c[i])):  #j gives the number of columns
        c[i][j]=a[i][j]+b[i][j]

#printing the sum
print("The sum of the two lists is: ",c)

