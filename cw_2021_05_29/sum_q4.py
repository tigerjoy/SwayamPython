def sum(n):
  if(0<=n<=9):
    return(n)                      #base case
  elif (n < 0):
    return -1
  else:
    return((n%10)+sum(n//10))  #reccursion case
          

a=int(input("Enter the number:"))
print("sum of digits of",a,"is",sum(a))