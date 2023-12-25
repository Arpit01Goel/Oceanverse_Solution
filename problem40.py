#Write a function that displays the spiral: RULLDDRRRUUULLLL… and so on. It should keep displaying until it has displayed 1,000,000 Letters in this pattern


def spiral(n):
    
    #First calculating enough stocks.
    #sum is n*(n-1)
    #let t=enough stocks
    t=1
    while t*(t-1)<n:
        t+=1

    ans=''

    for i in range(1,t+1):
        if (i%2):
            ans+="R"*i+"U"*i
        else:
            ans+="L"*i+"D"*i
    print(ans[0:n:1])


spiral(1000000)
