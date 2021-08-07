def rev_digits(n):
  rev=0
  while(n!=0):
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
  return(rev)

def is_palindrome(n):
  rev=rev_digits(n)
  for i in range(1,n+1):
    return(n==rev)

lb = int(input("Enter the lower bound: "))
ub = int(input("Enter the upper bound: "))

for i in range(lb, ub + 1):
  if is_palindrome(i):
    print(i, end=",")

