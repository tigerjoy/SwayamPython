n=int(input("Enter number of rows: "))
stars=n-1

for row in range(1,n+1):
  for col in range(1,row+1):
    print(col,end="")
  print("*"*stars,end="")
  stars=stars-1
  print()
