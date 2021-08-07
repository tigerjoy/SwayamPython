def is_prime(number):
  fact_count = 2
  for i in range(2,number):
    if(number%i==0):
      fact_count+=1
  # condition = true, ret = true
  # condition = false, ret = false
  return(fact_count==2)

def nprime(count):
  num=2
  while(True):
    if(is_prime(num)):
      print(num,end=",")
      count=count-1
    num=num+1
    if(count==0):
      break

nprime(10)
