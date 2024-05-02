a=[]
size=int(input("enter the number of list size"))
for i in range(size):
    a.append(int(input("Enter the data")))
print(a)

for j in a:
    if j%2!=0:
        print(j)
