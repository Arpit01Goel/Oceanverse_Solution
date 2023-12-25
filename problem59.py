#program to encrypt a string using zaesar cipher
from sys import argv
a=open(argv[1]).read()

b=input("Enter pattern")

d={}
for i in range(97,123):
    d[chr(i)]=b[i-97]
for i in range(65,91):
    d[chr(i)]=b[i-65+26]


def encrypt(a):
    b=''
    for i in a:
        if i=="\n":
            continue
        b+=d[i]
    return b

print(encrypt(a))
    
