#Write a function called find_max that takes a list of numbers and returns the largest number in the list.

def find_max(l):
    a=l[0]
    for i in l:
        if i>a:
            a=i
    return a

l=eval(input("Enter the list: "))
print(find_max(l))
