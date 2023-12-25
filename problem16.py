n1=input("Enter the sting") #take string as input
count=0
for i in n1:
    if i in {'a','e','i','o','u'}:  # list of vowels
        count+=1    #If vowel ,count it
print("no of vowels",count) #print no of vowels
print("no of consonants",len(n1)-count) #total - vowels is consonants
