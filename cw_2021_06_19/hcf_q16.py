def hcf(divisor,dividend):
  if dividend%divisor==0:
    return(divisor)
  else:
    return (hcf(dividend%divisor,divisor))
  
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))

print("HCF of", num1 ,"and",num2 ,"is",hcf(num1,num2))