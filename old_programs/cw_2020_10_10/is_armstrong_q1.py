def count_digits(n):
  count=0
  while(n!=0):
    count=count+1
    n=n//10
  return(count)

def is_armstrong(n):
  count=count_digits(n)
  sum=0
  n1=n
  while(n!=0):
    dig=n%10
    sum=sum + dig**count
    n=n//10
  return(n1==sum)

n=int(input("Enter a number:"))
if(is_armstrong(n)):
  print(n,"is an armstrong number.")
else:
  print(n,"is not an armstrong number.")


  