def hcf(num1,num2):
  divisor=num1
  dividend=num2
  rem=dividend%divisor
  while(rem != 0):
    dividend=divisor
    divisor=rem
    rem=dividend%divisor
  return(divisor)

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
print("HCF(",num1,",",num2,") =",hcf(num1,num2))

# HCF( 16 , 18 ) = 2




