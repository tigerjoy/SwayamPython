def last_digit(num1,num2):
  # if((num1%10)>(num2%10)):
  #   return(num2)
  # else:
  #   return(num1)

  # Alternative
  return num2 if((num1%10)>(num2%10)) else num1

num1=int(input("Enter the first numbers:"))
num2=int(input("Enter the second numbers:"))
print("the number having the minimum last digit is",last_digit(num1,num2))
