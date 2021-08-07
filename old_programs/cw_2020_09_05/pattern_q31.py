n=int(input("Enter number of rows: "))
spaces=0

for row in range(n,0,-1):
  print(" "*spaces,end="")
  for col in range(1,row+1):
    if(col%2==1):
      print("1",end="")
    else:
      print("0",end="")
  spaces=spaces+1
  print()