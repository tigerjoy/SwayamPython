a=float(input("enter the value of a: "))
b=float(input("enter the value of b: "))
c=float(input("enter the value of c: "))

discriminant=b**2-(4*a*c)

if discriminant>=0:
  print("Roots are real")
else:
  print("Roots are imaginary")