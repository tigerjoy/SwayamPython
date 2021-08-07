n=int(input("Enter number of rows: "))
spaces=n-1

for row in range(1,n+1):
  print(" "*spaces,end="")
  for col in range(1,row+1):
    print(chr(row+64),end="")
  spaces=spaces-1
  print()