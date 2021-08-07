x=int(input("Enter the x:"))
n=int(input("Enter the number of terms:"))

s=x
for i in range(2,n+1):
  if(i%2==0):
    s=s-(x**((2*i)))/((2*i))
  else:
    s=s+(x**((2*i)))/((2*i))

print("The sum of the series is:",s)