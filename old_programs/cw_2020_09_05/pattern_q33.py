n=int(input("Enter number of rows: "))
# k=65
# Alternative
k = 1

for row in range(1,n+1):
  for col in range(1,row+1):
    # print(chr(k),end="")
    # Alternative
    print(chr(k+64), end="")
    k=k+1
  print()