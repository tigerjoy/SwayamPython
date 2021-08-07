d1 = int(input("enter first date: "))
m1 = int(input("enter first month: "))
y1 = int(input("enter first year: "))
d2 = int(input("enter second date: "))
m2 = int(input("enter second month: "))
y2 = int(input("enter second year: "))

if (y1>y2) :
  print("Date 1 is greater")
elif (y1<y2) :
  print("Date 2 is greater")
elif (m1>m2) :
  print("Date 1 is greater")
elif (m1<m2) :
  print("Date 2 is greater")
elif (d1>d2) :
  print("Date 1 is greater")
elif (d1<d2) :
  print("Date 2 is greater")
else :
  print("the date are equal")