n=int(input("Enter number of rows: "))
space=n-1

for row in range(1,n+1):
  print(" "*space,end="")
  for col in range(1,row+1):
    print(col,end=" ")
  print()
  space=space-1