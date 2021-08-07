n=int(input("Enter number of rows: "))

for row in range(1,n+1):
  for col in range(1,row+1):
    print(row,end="")
  for col in range(row+1,n+1):
    print(col,end="")
  print()