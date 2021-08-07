def pow(a,b):
  if(b==0):
    return (1)               #base case
  else:
    return(a*pow(a,b-1))      #reccursion case

a=int(input("Enter the base:"))
b=int(input("Enter the index:"))

# 2 ^ 3 = 8
print(a,"^",b,"=",pow(a,b))