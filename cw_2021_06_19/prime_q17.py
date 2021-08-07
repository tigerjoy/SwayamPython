def is_prime(num,f=2):
  if(f>num):
    return(False)
  elif(num==f):
    return(True)
  elif(num%f==0 and num != f):
    return(False)
  else:
    return(is_prime(num,f+1))
  
num=int(input("Enter a number:"))
if(is_prime(num)):
  print("It is a prime number.")
else:
  print("It is not a prime number.")
