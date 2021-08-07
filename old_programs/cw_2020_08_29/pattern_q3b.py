n=int(input("Enter number of rows: "))
space=0

for row in range(1,n+1):
  print(" "*space,end="")
  for col in range(row,n+1):
    print("*",end="")
  print()
  space=space+1