def hcf(num1,num2):
  divisor=num1
  dividend=num2
  rem=dividend%divisor
  while(rem != 0):
    dividend=divisor
    divisor=rem
    rem=dividend%divisor
  return(divisor)

def lcm(num1,num2):
  return((num1*num2)//hcf(num1,num2))

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("LCM(", num1, ",", num2, ") = ", lcm(num1, num2))