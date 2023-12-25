#taking input of marks in 5 subjects
marks=[]
for i in range(1,6):
    marks.append(int(input(f"Enter marks in {i} subject")))
#calculate average
avg=0
for i in marks:
    avg+=i/5
# apply the conditions    
if avg>=90:
    print("A")
elif avg>=80:
    print("B")
elif avg>=70:
    print("C")
elif avg>=60:
    print("D")
else:
    print("F")
