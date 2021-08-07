def sum_digits(n):
  sum=0
  while(n!=0):
    dig=n%10
    sum=sum+dig
    n=n//10
  return(sum)

n=int(input("Enter a number:"))
print("The sum of digits of",n,"is:",sum_digits(n))