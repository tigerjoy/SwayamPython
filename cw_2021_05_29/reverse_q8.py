import math

def reverse(n):
  if(0<=n<=9):
    return(n)                      
  else:
    x = math.floor(math.log10(n))
    return((n%10)*(10**x)+reverse(n//10)) 
          

a=int(input("Enter the number:"))
# The reverse of 1769 is 9671
print("The reverse of ",a,"is",reverse(a))