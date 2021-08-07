n=int(input("Enter number of rows: "))

for row in range(n,0,-1):
  for col in range(row,0,-1):
    print(chr(col+64),end="")
  print()