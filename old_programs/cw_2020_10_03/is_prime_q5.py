def is_prime(n):
  count=0
  for i in range(1,n+1):
    if(n%i==0):
      count=count+1
  # if(count==2):
  #   return(True)
  # else:
  #   return(False)
  return count==2

n=int(input("Enter a number:"))

result=is_prime(n)

#True
# if(True):
#   print(1)
# else:
#   print(0)

# if(result==True):
if(result):
  print(n,"is prime.")
else:
  print(n,"is not prime.")