def power(a,b):
  pow=1
  for i in range(1,b+1):
    pow=pow*a
  return(pow)

a=int(input("Enter base: "))
b=int(input("Enter index: "))

# pow(2,3) = 8
print("pow(",a,",",b,")=",power(a,b))  