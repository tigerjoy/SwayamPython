n=int(input("Enter the number of terms:"))

s=2
for i in range(2,n+1):
  if(i%2==0):
    s=s+((i**3)-i)
  else:
    s=s+((i**3)+i)

print("The sum of the series is:",s)