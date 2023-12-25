#You are given the file sherlock.txt. You can consider any other big text file with english words, preferably a story book. Try reading the file and create a function which returns a string s which contains all the letters of sherlock.txt. You must remove all the non-letter characters from the file. 


#defining required function
def f(x):

    #open and read file
    a=open(x)
    b=a.read()
    #create s
    s=''
    #store letters in a set for instant search
    l=[]
    for i in range(65,92):
        l.append(chr(i))
    for i in range(97,123):
        l.append(chr(i))
    char=set(l)
    #check if letter is in char and add to s
    for i in b:
        if i in char:
            s+=i
    return s


#we know file name so no need to take input

s=f('sherlock.txt')
print(s)
