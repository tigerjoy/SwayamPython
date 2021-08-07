def generate(n):
  import random
  num=random.randint(10**(n-1),(10**n)-1)
  return(num)

n=int(input("Enter noumber of digits:"))
print(generate(n))