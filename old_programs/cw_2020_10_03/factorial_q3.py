def factorial(n):
  prod=1
  for i in range(n,1,-1):
    prod=prod*i
  return(prod)

n=int(input("Enter a number: "))

fact = factorial(n)

print("The factorial of",n,"is:",fact)






