def rev_digits(n):
  rev=0
  while(n!=0):
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
  return(rev)

n=int(input("Enter a number:"))
print("The reverse of",n,"is:",rev_digits(n))


