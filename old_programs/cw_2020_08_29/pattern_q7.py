n=int(input("Enter number of rows: "))

for row in range(n,0,-1):
  for col in range(n,row-1,-1):
    print(col,end=" ")
  print()