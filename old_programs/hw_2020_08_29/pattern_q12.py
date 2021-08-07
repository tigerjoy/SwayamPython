n=int(input("Enter number of rows: "))
spaces= n-1

for row in range(1,n+1):
  print("  " * spaces, end=" ")
  # 1st Half
  for col in range(1,row+1):
    print(col,end=" ")
  # 2nd Half
  for col in range(row-1,0,-1):
    print(col,end=" ")
  spaces=spaces-1
  print()