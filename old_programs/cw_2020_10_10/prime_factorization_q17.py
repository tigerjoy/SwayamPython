def prime_fact(num):
  factor=2
  while(num!=1):
    if(num%factor==0):
      print(factor,end=",")
      num=num//factor
    else:
      factor=factor+1
  

num=int(input("Enter a number:"))
print("The prime factorization of",num,"is: ",end=" ")
prime_fact(num)