def perfect_number(n):
  sum = 0
  for i in range(1, n):
    if (n % i == 0):
      sum = sum + i
  return(sum == n)

lb = int(input("Enter the lower bound: "))
ub = int(input("Enter the upper bound: "))

for i in range(lb, ub + 1):
  if perfect_number(i):
    print(i, end=",")
