lb=int(input("enter lower bound: "))
ub=int(input("enter upper bound: "))

print("Displaying numbers in asending order")
i=lb
while(i<=ub):
  print(i,end=",")
  i=i+1

# To go to the next line
print()

print("Displaying numbers in desending order")
i=ub
while(i>=lb):
  print(i,end=",")
  i=i-1

  
  