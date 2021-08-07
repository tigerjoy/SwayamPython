import sys

def fact(n):
  if(n==1):
    return (1)               #base case
  else:
    return(n*fact(n-1))      #reccursion case

sys.setrecursionlimit(1000)

n=int(input("Enter a number:"))
print(n,"! =",fact(n))