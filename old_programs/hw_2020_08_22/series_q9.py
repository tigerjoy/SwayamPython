n=int(input("Enter the number of terms:"))

s=1
for i in range(2,n+1):
  s=s+(1/(i**3))

print("The sum of the series is:",s)