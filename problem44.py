#Consider the data of Height and Weight of 25,000 people as available here. Is the data correlated? What is the correlation? Can you plot the points and fit a line? You are free to use any built in functions, but you should know what the functions are doing. Correlation is a statistical concept which you may know from your high school, we only expect you to understand this concept at an intuitive level

#FILE HANDELING
#import data from the given file using inbuild funcions
a=open("SOCR-HeightWeight.csv").read()

#now to handel it in python easily , modify its form 
b=a.split(sep='\n')
#this will make each entry different 

#below will create a perfect 2 D array 
for i in range(len(b)):
    b[i]=b[i].split(sep=',')


#now delete headers of file
del b[0]







#NOW PLOT GRAPH

#use matplotli
import matplotlib.pyplot as plt

#take height on x axis and weight on y axis

#to reduce time , iterate over list only once

X=[];Y=[]




















#FIND CORELATION


#now first find co-relation

#first find mean of height and weight

#mean of height,h
h=0
for i in range(len(b)):
    h+=float(b[i][1])


h=h/len(b)

#mean of weight,w
w=0
for i in range(len(b)):
    w+=float(b[i][2])

w=w/len(b)

#now find co-relation
#co-relation is given by
#r=( sum of all (x-h)(y-w) )/sqrt((sum of all (x-h)**2 )*(sum of all (y-w)**2))        where x is individual height and w is same persons weight


#to reduce time , iterate over list only once
#take numenator as n and denominator as m
#we will firsst calculate m1 and m2 then m and then take square root
n=m=m1=m2=0

for [i,x,y] in b:
    x,y=float(x),float(y)
    n+=(x-h)*(y-w)
    m1+=(x-h)**2
    m2+=(y-w)**2
    X.append(x);Y.append(y)
#now calculate denominator
m=(m1*m2)**(0.5)

#calculate corelation coefficient
r=n/m

print(f"Coefficient of corelation is {r}")
plt.scatter(X,Y,s=0.1)

#give name to axis
plt.xlabel("Height")
plt.ylabel("Weight")

#plt.show() command to show graph

plt.show()
