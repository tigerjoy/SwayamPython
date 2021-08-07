def convert(amount_in_dollar,conversion_rate):
  amount_in_rupee=amount_in_dollar*conversion_rate
  print(amount_in_rupee)

def convert2(amount_in_dollar,conversion_rate):
  amount_in_rupee=amount_in_dollar*conversion_rate
  return(amount_in_rupee)

amount_in_dollar=float(input("Enter ammount in dollars:"))
conversion_rate=float(input("Enter convertion rate:"))

convert(amount_in_dollar,conversion_rate)
print(convert2(amount_in_dollar,conversion_rate))