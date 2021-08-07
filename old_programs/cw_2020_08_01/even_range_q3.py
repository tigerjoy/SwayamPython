lb=int(input("enter lower bound: "))
ub=int(input("enter upper bound: "))

i=lb
while(i<=ub):
  if(i%2==0):
    print(i,end=",")
  i=i+1
  