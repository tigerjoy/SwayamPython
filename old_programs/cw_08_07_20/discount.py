total_cost=int(input("Enter total cost of items purchased: "))

if total_cost<=2000:
  assured_gift="Wall Clock"
  discount=total_cost*(5/100)
elif total_cost>=2001 and total_cost<=5000:
  assured_gift="School Bag"
  discount=total_cost*(10/100)
elif total_cost>=5001 and total_cost<=10000:
  assured_gift="Electric Iron"
  discount=total_cost*(15/100)
else:
  assured_gift="Wrist Watch"
  discount=total_cost*(20/100)

amount= total_cost-discount

print("Discount=",discount)
print("Assured gift=",assured_gift)
print('Amount Payable=',amount)