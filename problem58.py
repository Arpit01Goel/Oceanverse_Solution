#We solved the SFC question a while ago. Can you solve this on similar lines?

#we will use recursion to make the dirctional string
#base value of recursion(value at n=1 is given)

#to go to next pattern , there are a lots of stweps required
#so define funciton for ezch of them

#define upside down function
def upside_down(s):
    ans=''
    d={'U':'D','D':'U','L':'L','R':'R'}
    for i in s:
        ans+=d[i]
    return ans

#define a funciton which will reverse the direction of motion (end point will become first point and first point become end point)
def reverse(s):
    ans=''
    d={'U':'D','D':'U','L':'R','R':'L'}
    for i in s:
        ans+=d[i]
    return ans[::-1]

#now define main function which will call all the above functions
def curve(n):
    if n==1:
        return 'URDRU'
    else:
        #save previous pattern in a string to save time by not calling the function again and again
        t=curve(n-1)
        #now return the pattern with is observed
        return t+'U'+reverse(upside_down(t))+'U'+t+'R'+upside_down(t)+'D'+reverse(t)+'D'+upside_down(t)+'R'+t+'U'+reverse(upside_down(t))+'U'+t

#now take input from user
n=int(input())

#call the main function
print(curve(n))

