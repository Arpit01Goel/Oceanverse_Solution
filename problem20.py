y=int(input("Enter number of lines and curvature")) #no of lines will be integer
x=float(input()) #curvature can be float
def abs(x): #absolute value function
    if x>0:
        return x
    else:
        return -1*x
if x>0: #print * at required distance from left side of screen. distance comes using basic maths
    for i in range(y):
        print(" "*int(((y/2-i)**2)*x),"*")
else:
    x=abs(x) # let -ve part be handeled by maths and take magnitude only
    for i in range(y):
        t=((y/2)**2)*x # almost maximam no of charactes to be printed in one line(including spaces) . Take this like a work space.
        if i<y/2:
            print(" "*int(t-((y/2-i)**2)*x),"*") #now since y axis is right side of screen, calcute parabolic distance from right side.To do this, remove parabolic space from workspace.
            
        else:
            print(" "*int(t-(abs(y/2-i)**2)*x),"*")

