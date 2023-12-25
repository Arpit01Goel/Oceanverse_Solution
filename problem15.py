#defining required function. create y which is reverse of x and check if reverse is same as original
def check_palindrome(x):
    y=''
    for i in range(1,len(x)+1):
        y+=x[-i]
    return x==y

n1=input("Enter string")
print(check_palindrome(n1))
