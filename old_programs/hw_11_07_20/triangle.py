# CORRECTION
# DONE BY RANAJOY
# START
print("Calculate Area")
print("Press 1 for Equilateral Triangle")
print("Press 2 for Isosceles Triangle")
print("Press 3 for Scalene Triangle")
print("Press 4 for quit")
# END
choice=int(input("enter choice:"))

if choice==1:
  side=float(input("enter side: "))
  area=((3**0.5)/4)*side*side
  print("Area of the triangle is:",area)

elif choice==2:
  side=float(input("enter side: "))
  base=float(input("enter base: "))
  area=1/4*base*(4*side*side-base*base)**0.5
  print("Area of the triangle is:",area)

elif choice==3:
  side1=float(input("enter 1st side: "))
  side2=float(input("enter 2nd side: "))
  side3=float(input("enter 3rd side: "))
  s=(side1+side2+side3)/2
  area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
  print("Area of the triangle is:",area)

elif choice == 4:
  print("Quiting...")
else:
  print("Wrong choice")