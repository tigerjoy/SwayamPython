lb=int(input("enter lower bound: "))
ub=int(input("enter upper bound: "))

print(" even Numbers are in ascending order:")
for i in range(lb,ub+1):
  if(i%2==0):
    print(i,end=",")