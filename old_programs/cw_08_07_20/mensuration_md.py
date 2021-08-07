length=float(input("Enter length of rectangle: "))
breadth=float(input("Enter breadth of rectangle: "))

print("Press 1 to display area")
print("Press 2 to display perimeter")
print("Press 3 to display diagonal")
print("Press 4 to quit")

choice=int(input("enter your choice: "))

if(choice==1):
  print('The area of the rectangle is',(length*breadth))
elif(choice==2):
  print('The perimeter of the rectangle is',2*(length+breadth))
elif(choice==3):
  diagonal=(length**2 + breadth**2)**(1/2)
  print('The diagonal of the rectangle is',diagonal)
elif(choice==4):
  print('Quiting')
else:
  print('Invalid choice')

