def avg(*args):
  sum=0
  for item in args:
    sum=sum+item
  avg=sum/len(args)
  return(avg)

print("avg(1,2,3): ", avg(1,2,3))
print("avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ", 
avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

