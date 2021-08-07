def count(n):
  if(0<=n<10):
    return(1)
  else:
    return(1+count(n//10))

a=int(input("Enter the number:"))
# The number of digits in 1796 is 4
print("The number of digits in",a,"is",count(a))