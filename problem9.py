n=int(input("Enter the number"))
i,j=int(input("Enter the value of starting of times table")),int(input("Enter the value of end of times table"))
for k in range(i,j+1):
    print(f"{n} X {k} ={n*k}")
