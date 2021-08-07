def is_prime(n):
  count=0
  for i in range(1,n+1):
    if(n%i==0):
      count=count+1
  return count==2

def prime_factors(n):
  for i in range(1,n+1):
    if(n%i==0):
      if(is_prime(i)):
        print(i,end=",")

n=int(input("Enter a number:"))
print("The prime factors of {} are:".format(n), end=" ")
prime_factors(n)
