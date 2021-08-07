age = int(input("Enter age: "))
ti = int(input("Enter taxable income: "))
gender = input("Enter gender: ")

if (age>65 or gender=='F'):
  print("wrong category")
elif (age<=65 and gender=='M'):
  if (ti<=160000):
    income_tax = 0 
  elif(ti>160000 and ti<=500000):
    income_tax = (ti-160000) * (10/100)
  elif(ti>500000 and ti<=800000):
    income_tax = ((ti - 500000) * (20/100)) + 34000 
  else :
    income_tax = ((ti - 800000) * (30/100)) + 94000
  print ("Tax payable= ₹",income_tax)
  