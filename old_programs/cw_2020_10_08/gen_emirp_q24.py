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
  return is_prime(n) and is_prime(rev_n)

lb=int(input("Enter the lower bound: "))
ub=int(input("Enter the upper bound: "))

print("\nThe emirp numbers between", lb, "to", ub, "are")
for i in range(lb,ub + 1):
  if(is_emirp(i)):
    print(i,end=",")

print()

