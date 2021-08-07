def rev_digits(n):
  rev=0
  while(n!=0):
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
  return(rev)

def is_palindrome(n):
  rev=rev_digits(n)
  return(n==rev)

n=int(input("Enter a number:"))

if(is_palindrome(n)):
  print(n,"is palindrome.")
else:
  print(n,"is not palindrome.")


