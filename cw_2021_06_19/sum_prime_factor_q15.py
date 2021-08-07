def sum_prime_factors(num,f=2):
  if num==1:
    return(0)
  elif(num%f==0):
    return(f+sum_prime_factors(num//f,f))
  else:
    return(sum_prime_factors(num,f+1))
  
num=int(input("Enter a number:"))

print("Sum of prime factors of", num ,"is:", sum_prime_factors(num))
