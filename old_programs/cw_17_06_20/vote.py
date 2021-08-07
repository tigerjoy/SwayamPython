age = int(input("Enter your age: "))

if age >= 18:
  print("You are eligible to vote!")
else:
  x = 18 - age
  print("Come back after", x, "years")