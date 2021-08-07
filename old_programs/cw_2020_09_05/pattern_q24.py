n=int(input("Enter number of rows: "))

for row in range(1,n+1):
  for col in range(1,row+1):
    if(row%2==1):
      if(col%2==1):
        print("1",end="")
      else:
        print("0",end="")
    else:
      if(col%2==1):
        print("0",end="")
      else:
        print("1",end="")         
  print()
