lb=int(input("enter lower bound: "))
ub=int(input("enter upper bound: "))

print("Numbers are in ascending order:")
for i in range(lb,ub+1):
  print(i,end=",")

print("\nNumbers are in desending order:")
for i in range(ub,lb-1,-1):
  print(i,end=",")
  

  