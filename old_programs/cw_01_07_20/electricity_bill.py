consumer_no = input("Enter the consumer number: ")
consumer_name = input("Enter the consumer name: ")
units = int(input("Enter the units consumed: "))

if (units<=100):
  amount = 5.5*units
elif (units>100 and units<=300):
  amount = (5.5 * 100) + 6.5*(units-100)
elif (units>300 and units<=600):
  amount = (5.5 * 100) + (6.5 * 200) + 7.5*(units-300)
else :
  amount = (5.5 * 100) +(6.5 * 200) + (7.5 * 300 )+ 8.5*(units-600)

print("\t\t\tMoney recipt")
print("Consumer's number: ",consumer_no)
print("Consumer's name: ",consumer_name)
print("Units consumed: ",units)
print("Amount to be paid: ₹",amount)





