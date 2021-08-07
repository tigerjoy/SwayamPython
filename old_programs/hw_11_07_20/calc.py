# CORRECTION
# DONE BY RANAJOY
# START
print("Press 1 to add")
print("Press 2 to subtract")
print("Press 3 to multiply")
print("Press 4 to divide")
print("Press 5 to calculate remainder")
print("Press 6 to quit")
# END
choice = int(input("Enter your choice:")) 
num1 = int(input("Enter first numbers: "))
num2 = int(input("Enter second numbers: "))

if choice == 1: 
  sum = num1 + num2
  print("Result = ", sum)

elif choice == 2: 
  dif = num1 - num2
  print("Result = ", dif)

elif choice == 3: 
  pro = num1 * num2
  print("Result = ", pro)

elif choice == 4: 
  div = num1 / num2
  print("Result = ", div)

elif choice == 5: 
  rem = num1 % num2
  print("Result = ", rem)
 
elif choice == 6:
    exit()

else:
  print("Wrong input")