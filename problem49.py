#Write a function that reads a file which has numbers in each line and outputs it on the screen one by one.

#take argumetn from user the file name of the file to read

from sys import argv

#as argv will take problem49.py as first argument so we will take second argument as file name
name=argv[1]

#now define required function

def read_file(file_name):
    #this function will read file (argument is file name) and pritn each line one by one

    #read file 
    f=open(file_name)
    f1=f.read()

    #split the file into lines
    f2=f1.split("\n")

    #print each line one by one
    for i in f2:
        print(i,end=" ")
        t=input()

#now do the required task
print("press enter to print next line")
read_file(name)
