n=int(input("Enter the number of terms:"))

s=1
for i in range(2,n+1):
  if(i%2==0):
    s=s-((2*i)-1)
  else:
    s=s+((2*i)-1)

print("The sum of the series is:",s)