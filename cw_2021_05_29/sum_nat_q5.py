def sum_nat(n):
  if(n==1):
    return(1) 
  elif(n<1):
    return(0)                   #base case
  else:
    return(n+sum_nat(n-1))  #reccursion case
          

a=int(input("Enter the number:"))
# The sum of natural nos upto 5 is 15
print("sum of natural numbers upto",a,"is",sum_nat(a))