def product(n):
  if(0<=n<=9):
    return(n)                      #base case
  elif (n < 0):
    return -1
  else:
    return((n%10)*product(n//10))  #reccursion case
          

a=int(input("Enter the number:"))

# Product of digits 45 is 20
print("product of digits of",a,"is",product(a))