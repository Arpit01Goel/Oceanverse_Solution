#27. Create a Python program that prompts the user for their age. If the age is less than 18, print “You are a minor.” If the age is between 18 and 65, print “You are an adult.” Otherwise, print “You are a senior citizen.”





age=int(input("Enter the age"))   #take input
#apply conditions one by one 
if age<18:  
    print("You are a minor")
elif age<66:
    print("You are an adult")
else:
    print("You are a senior citizen")
