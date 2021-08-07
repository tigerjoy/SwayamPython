x = 5
def calcSum(a, b, c):
  return a + b + c

def average(x, y, z):
  return (x + y + z) / 3

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
print("Average:", average(num1, num2, num3))
print("Sum:", calcSum(num1, num2, num3))

