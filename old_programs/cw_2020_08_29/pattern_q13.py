n=int(input("Enter number of rows: "))
k=1

for row in range(1,n+1):
  for col in range(row,0,-1):
    print(k,end=" ")
    k=k+1
  print()