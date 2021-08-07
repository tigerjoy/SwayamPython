def rev_dig(n):
  rev=0
  while(n!=0):
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
  return(rev)

def is_prime(n):
  count=0
  for i in range(1,n+1):
    if(n%i==0):
      count=count+1
  return(count==2)

def is_emirp(n):
  rev_n=rev_dig(n)
  # if(is_prime(n) and is_prime(rev_n)):
  #   return(True)
  # else:
  #   return(False)
  # Alternative
  return is_prime(n) and is_prime(rev_n)

n=int(input("Enter a number: "))
if(is_emirp(n)):
  print(n,"is an emrip number")
else:
  print(n,"is not an emrip number")  

