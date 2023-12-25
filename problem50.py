#program to define a funciton named sfc as described in the question

#AS observing figure, a patter n is observed
#Any figure except first one can be obtained by previous figure and doing operations on it which remains same

#first define functions to do the operations

#insted of defining whole code in co ordinate system, we can define it by direction of motion and in the end, we will calculate co-ordinates by moving in that direction



def rotate_counter(s):
    #s is a string of directions.This function will rotate the figure in counter clockwise direction
    d={'U':'R','L':'U','D':'L','R':'D'}
    #store new direction set in new_s
    new_s=''
    #write new direction
    for i in s:
        new_s+=d[i]
    #now executon is done in reverse order as starting point is used last
    return new_s[::-1]
def rotate_clock(s):
    #s is a string of directions.This function will rotate the figure in clockwise direction
    d={'U':'L','R':'U','D':'R','L':'D'}
    #store new direction set in new_s
    new_s=''
    #write new direction
    for i in s:
        new_s+=d[i]
    #now executon is done in reverse order as ending point is used first
    return new_s[::-1]

#now define main function
def sfc(n):
    #n is the number of steps
    #define base case
    if n==1:
        return 'DRU'
    else:
        #as described, figure depends upon previous figure
        a=sfc(n-1)
        #next statement is as per observation which may not be found by logic or my program
        return rotate_counter(a)+'D'+a+'R'+a+'U'+rotate_clock(a)

#now define a function to calculate co-ordinates
def co_ordinate(s):
    #s is a string of directions
    #co-ordinates are returned as a tuple
    x=1
    y=1
    #store co-ordinates in a list
    #inintially at (1,1)
    data=[(1,1)]
    for i in s:
        #These 4 are as per question
        if i=='D':
            x+=1
            data.append((x,y))
        elif i=='U':
            x-=1
            data.append((x,y))
        elif i=='R':
            y+=1
            data.append((x,y))
        else:
            y-=1
            data.append((x,y))
    return data


#now take input from user
n=int(input('Enter the number of steps: '))
#store the directions in s
s=sfc(n)
#print the co-oridnates
print(co_ordinate(s))

    


