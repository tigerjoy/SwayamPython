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

lb=int(input("Enter the lower bound: "))
ub=int(input("Enter the upper bound: "))

print("\nThe armstrong numbers between", lb, "to", ub, "are",end="")

for i in range(lb,ub + 1):
  if(is_armstrong(i)):
    print(i,end=",")


