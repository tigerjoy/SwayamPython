num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
num3=int(input("enter third number :"))

if num1>=num2 and num1>=num3:
  print("greatest number is",num1)
elif num2>=num1 and num2>=num3:
  print("greatest number is",num2)
else:
  print("greatest number is",num3)

if num1<=num2 and num1<=num3:
  print("smallest number is",num1)
elif num2<=num1 and num2<=num3:
  print("smallest number is",num2)
else:
  print("smallest number is",num3)