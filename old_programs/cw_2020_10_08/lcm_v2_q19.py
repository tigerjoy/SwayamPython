def lcm(num1, num2):
  factor = 2
  lcm = 1

  while num1 != 1 or num2 != 1:
    if num1 % factor == 0 and num2 % factor == 0:
      lcm = lcm * factor
      num1 = num1 // factor
      num2 = num2 // factor
    elif num2 % factor == 0:
      lcm = lcm * factor
      num2 = num2 // factor
    elif num1 % factor == 0:
      lcm = lcm * factor
      num1 = num1 // factor
    else:
      factor = factor + 1
  
  return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("LCM(", num1, ",", num2, ") = ", lcm(num1, num2))