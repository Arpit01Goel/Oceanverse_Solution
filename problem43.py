#Consider the sensex data from here. Consider only the end of the day closing values. When should you have bought and when should you have sold in order to gain the maximum return in this 30 year period? You can assume that you can buy the stocks partially and you start with, let us say 1,00,000 Rupees. (10 points)

#Defining variable bank_bal which will record my balance all the time
#Defining no of stocks
#these two are my assests

bank_bal=100000
no_of_stocks=0

#putting prices in a list
a=open("BSE Sensex Daily Close Jan1990 Oct2020.csv").read()
b=a.split(sep=',')
data=[]
day_date=[]
for i in range(8,len(b),5):
    data.append(float(b[i]));day_date.append(b[i-4])


#calculate no of days
t=len(data)
#print(data)
#deduction on which day to start

print(f"initial bank balance is {bank_bal}")


for i in range(t-1):
    #print(data[i])
    if data[i+1]>data[i]:
        bank_bal,no_of_stocks=0,bank_bal/data[i]
        start_day=i
        print(f"start on dayno {start_day}")
        print(f"no of stocks is :{no_of_stocks}")
        break

#for each day if price decrease next day,sell all stocks.
#if price increase next day,purchase

#saving data in lists
sale_days=[]
purchase_days=[]
for i in range(start_day,t):
    try:
        if data[i+1]<data[i]:
            if no_of_stocks==0:
                pass
            else:
                bank_bal,no_of_stocks=no_of_stocks*data[i],0
                sale_days.append(i)
                print("On day ",i,"stocks are sold",end=" ")
                print("money is ",bank_bal) 
        else:
            if bank_bal>0:
                bank_bal,no_of_stocks=0,bank_bal/data[i]
                purchase_days.append(i)
                print("On day ",i,"stocks are purchased",end=" ")
                print("stocks are ",no_of_stocks)
    except IndexError:
        pass
else:
    if no_of_stocks>0:
        bank_bal,no_of_stocks=data[-1]*no_of_stocks,0;sale_days.append(i)

print(sale_days[0:10])
print(purchase_days[0:10])
print(f"final bank balance is {bank_bal}")

print(sale_days[-10:])
print(purchase_days[-10:])



