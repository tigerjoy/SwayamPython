def calcSum(x, y):
  z = x + y
  print(globals())
  print(locals())
  return z

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
sum = calcSum(num1, num2)
print("Sum of given numbers is", sum)


