#Write a function that takes as inputs list of lists that depicts square matrices A and B and then gives us the product.

#take both input
a=eval(input("Enter the first matrix: "))
b=eval(input("Enter the second matrix: "))

#writing a function to multiply two lists as its done in matrix multiplication
def mul(a,b):
    #function to multiply two lists
    t=0
    for i in range(len(a)):
        t+=a[i]*b[i]
    return t

#writing a function to multiply two matrices
def multiply(x,y):
    #This function multiple two matrices x and y in order

    #calculate the order of new matrix c and make its structure
    #calculate the dimentions of c
    c1=len(x)  #as per definition of matrix multiplication
    c2=len(y[0]) #as per definition of matrix multiplication

    #calculate dimention of vector to be multiplied
    c3=len(y)
    #make the structure of c
    c=[]
    
    for i in range(c1):
        c.append([0 for j in range(c2)])    #insert zeroes(=no of columns ) no of rows times
    #structure of c is ready   
    
    #multiply the matrices
    for i in range(c1):
        for j in range(c2):
            a=x[i]
            b=[]
            for k in range(c3):
                b.append(y[k][j])
            c[i][j]=mul(a,b)
    return c

#print required result
print(multiply(a,b))

