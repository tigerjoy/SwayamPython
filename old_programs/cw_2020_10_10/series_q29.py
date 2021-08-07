def factorial(n):
  prod=1
  for i in range(n,1,-1):
    prod=prod*i
  return(prod)

n=int(input("Enter number of terms:"))
x=int(input("Enter the value of x:"))
s=1
for i in range(2,n+1):
  s=s+((x**(2*i-3))/factorial(i-1))
print("The sum of series is :",s)