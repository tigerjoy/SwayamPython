n=int(input("Enter the number of terms:"))

s=2
for i in range(2,n+1):
  if(i%2==0):
    s=s-(2*i)
  else:
    s=s+(i*2)

print("The sum of the series is:",s)