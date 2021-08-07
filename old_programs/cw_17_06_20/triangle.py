# To check if a triangle is possible or not we need to
# see, whether the sum of any two sides is greater
# than the thrid side.

side1=int(input("enter first side of the triangle :"))
side2=int(input("enter second side of the triangle :"))
side3=int(input("enter third side of the triangle :"))

if side1<(side2+side3) and side2<(side1+side3) and side3<(side2+side1):
  print("a triangle is possible")
  if side1==side2==side3:
    print("it is a equilateral triangle")
  elif side1==side2 or side2==side3 or side1==side3:
    print("it is a isoceles triangle")
  else:
    print("it is a Scalene triangle")  

else:
  print("a triangle is not possible")
