def print_digits(n):
  while(n!=0):
    dig=n%10
    print(dig)
    n=n//10

n=int(input("Enter a number:"))
print("The digits of",n,"are:")
print_digits(n)






