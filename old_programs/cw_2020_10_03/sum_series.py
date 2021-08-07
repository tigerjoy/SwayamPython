def sum_series(n):
  s = 1
  for i in range(2, n + 1):
    s = s + i
  return s

n = int(input("Enter the number of terms: "))

s = sum_series(n) # Function Call

print("Sum of series is", s)

# s = 1
# for i in range(2, n + 1):
#   s = s + i

