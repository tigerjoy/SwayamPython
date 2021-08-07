def count_digits(n):
  count=0
  while(n!=0):
    count=count+1
    n=n//10
  return(count)

n=int(input("Enter a number:"))
print("The number of digits of",n,"are:",count_digits(n))
