# def high(lst):
#   max=lst[0]
#   max2=None
#   for i in range(1,len(lst)):
#     if(max<lst[i]):
#       max2=max
#       max=lst[i]
#     elif(max2 is None or max2<lst[i]):
#       max2=lst[i]
#   return(max,max2)

def two_high(num1, num2, *args):
  if num1 > num2:
    max=num1
    max2=num2
  else:
    max=num2
    max2=num1

  for i in range(0,len(args)):
    if(max<args[i]):
      max2=max
      max=args[i]
    elif(max2 is None or max2<args[i]):
      max2=args[i]

  return(max,max2)

lst=(1,)
print(two_high(*lst))
