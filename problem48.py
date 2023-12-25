#write a function that writes the first n numbers and writes it to a file by name output.txt
#this program takes the value of n from command line

def first_n(n):
    
    #open the file or overwrite if already exists
    f=open("output.txt",'w')
    
    #create content to write
    s=''
    for i in range(1,n+1):
        s+=str(i)+' '

    #now save the content to file
    f.write(s)

#take the value of n from user
from sys import argv

n=int(argv[1])

#do the task
first_n(n)

