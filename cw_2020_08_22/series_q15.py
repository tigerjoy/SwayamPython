n=int(input("Enter the number of terms:"))
a=int(input("Enter the value of a:"))

s=a/2
for i in range(3,n+1):
  s=s+(a/i+1)

print("The sum of the series is:",s)