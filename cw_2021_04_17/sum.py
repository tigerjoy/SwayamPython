def sum(*args):
  sum=0
  for item in args:
    sum=sum+item
  return(sum)

print("sum(2,4,5,6) =", sum(2,4,5,6))
print("sum(2,4,5,6,9,10) =", sum(2,4,5,6,9,10))
print("sum(2,4,5,6,'A') =", sum(2,4,5,6,'A'))

