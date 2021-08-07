def is_prime(n):
  count=0
  for i in range(1,n+1):
    if(n%i==0):
      count=count+1
  return count==2

lb = int(input("Enter the lower bound: "))
ub = int(input("Enter the upper bound: "))

for i in range(lb, ub + 1):
  if is_prime(i):
    print(i, end=",")

print()