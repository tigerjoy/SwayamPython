import random

def ran(x):
  a=10**(x-1)
  # COMMENT BY Ranajoy:
  """
    randint(a,b) generates a random number between [a, b] (both included). Hence, for this problem
    one should generate numbers between 10^(n-1) and (10 ^ n) - 1 and not (10 ^ n).
  """
  b=10**(x)
  print(random.randint(a,b))

n=int(input("Enter number of digit:"))

ran(n)