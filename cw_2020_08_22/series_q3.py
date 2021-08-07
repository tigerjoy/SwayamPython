n=int(input("Enter the number of terms:"))

s=1/2
for i in range(2,n+1):
  s=s+(i/(i+1))

print("The sum of the series is:",s)