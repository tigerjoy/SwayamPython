def avg(*args):
  sum=0
  for item in args:
    sum=sum+item
  avg=sum/len(args)
  return(avg)

arr = [1,2,3,4,5]

print("arr:", arr)
print("*arr:", *arr)
print("avg:", avg(*arr))