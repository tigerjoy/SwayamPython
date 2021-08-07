def root(x,n=2):
  print("{:.2f}".format(x**(1/n)))

x=int(input("Enter a number:"))
n=int(input("Enter nth Root:"))

if(n==0):
  root(x)
else :
  root(x,n)