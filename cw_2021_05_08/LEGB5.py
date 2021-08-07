def isPrime(num):
  for i in range(2, num+1):
    if num % i == 0:
      if num == i:
        result = True
      else:
        result = False
      break
  return result    

print("isPrime(5) =", isPrime(5))
print("isPrime(9) =", isPrime(9))

