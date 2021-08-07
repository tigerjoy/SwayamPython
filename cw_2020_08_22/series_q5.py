n=int(input("Enter the number of terms:"))
a=int(input("Enter the value of a:"))

s=a
for i in range(2,n+1):
  s=s+(a/i)

print("The sum of the series is:",s)