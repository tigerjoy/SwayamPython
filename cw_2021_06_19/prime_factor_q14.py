def prime_factors(num,f=2):
  if num==1:
    return
  elif(num%f==0):
    print(f)
    prime_factors(num//f,f)
  else:
    prime_factors(num,f+1)
  
num=int(input("Enter a number:"))

print("Prime factors of", num ,"is:")
prime_factors(num)