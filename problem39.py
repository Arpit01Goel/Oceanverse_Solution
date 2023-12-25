#program to calculate area of a circle
#take radius as input
r=float(input("Enter radius"))
#use Leibnix's Formula to calculate pi
pi=0
for i in range(1,1000000):
    pi+=4*((-1)**(i-1)/(2*i-1))
#formula for area is pi*(r squared)
def circle_area(r):
    return pi*r*r
print(circle_area(r))
