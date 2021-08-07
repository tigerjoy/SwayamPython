n=int(input("Enter number of rows: "))

for row in range(1,n+1):
  for col in range(row,n+1):
    # print(chr(col+64),end="")
    # Alternative
    print(chr(col + ord('A') - 1), end="")
  print()