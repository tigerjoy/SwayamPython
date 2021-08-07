def fibo(n):
  if(n==1):
    print("0")
  elif(n==2):
    print("0,1")
  else:
    print("0,1,",end="")
    t1=0
    t2=1
    for i in range(1, n-1): 
      t3=t1+t2
      t1=t2
      t2=t3
      print(t3,end=",")
  print()

n=int(input("Enter number of terms:"))
print("The fibonacii numbers are:")
fibo(n)
