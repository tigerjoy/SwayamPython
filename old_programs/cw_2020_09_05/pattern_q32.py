n=int(input("Enter number of rows: "))

for row in range(1,n+1):
  for col in range(1,row+1):
    if(col%2==1):
      print("*",end="")
    else:
      print("#",end="")
  print()
