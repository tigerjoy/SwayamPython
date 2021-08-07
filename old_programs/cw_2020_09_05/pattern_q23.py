n=int(input("Enter number of rows: "))

for row in range(n,0,-1):
  for col in range(1,2*row):
    print(col,end="")
  print()