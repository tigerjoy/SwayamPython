def perfect_number(n):
  sum = 0
  for i in range(1, n):
    if (n % i == 0):
      sum = sum + i
  return(sum == n)

n=int(input("Enter a number:"))
print(perfect_number(n))