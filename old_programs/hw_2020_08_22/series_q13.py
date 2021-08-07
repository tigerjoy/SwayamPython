n=int(input("Enter the number of terms:"))

s=0.25
for i in range(2,n+1):
  s=s+(i/((i+1)**2))

print("The sum of the series is:",s)