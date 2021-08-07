# def printFactorial(num):
#   fact = 1
#   i = num
#   while i >= 1:
#     fact = fact * i;
#     i -= 1
#   print(num, "! = ", fact, sep="") 

# def printFactorial(num):
#   fact = 1
#   i = num
#   while i >= 1:
#     fact = fact * i;
#     i -= 1
#   return fact

def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num - 1)

def recFactorial(num, fact, i):
  if i < 1:
    return fact
  else:
    fact = fact * i
    i -= 1
    return recFactorial(num, fact, i)

def isPrime(num):
  fact_count = 0
  i = 1
  while i <= num:
    if num % i == 0:
      fact_count += 1
    i += 1
  return fact_count == 0