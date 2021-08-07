def is_prime(n):
  count=0
  for i in range(1,n+1):
    if(n%i==0):
      count=count+1
  return (count==2)
    
def print_factors(num):
  for i in range(1, num + 1):
    # If i is a factor of num
    if num % i == 0:
      if is_prime(i):
        print(i, end=",")

n= int(input("enter a number:"))
# is_prime(n)
print_factors(n)