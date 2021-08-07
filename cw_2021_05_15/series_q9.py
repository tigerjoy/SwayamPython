def series(num1,num2):
  d=(num2-num1)/3
  print(num1,num1+d,num2-d,num2)

num1=int(input("Enter first numbers:"))
num2=int(input("Enter last numbers:"))
series(num1,num2)