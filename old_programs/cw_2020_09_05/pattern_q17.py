n=int(input("Enter number of rows: "))

for row in range(1,n+1):
  for col in range(n,row-1,-1):
    print("A",end="")
  print()