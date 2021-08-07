def display_range(lb, ub):
  print("The numbers in a range are")
  for i in range(lb, ub + 1):
    print(i, end=",")

  print()

lb = int(input("Enter the lower bound: "))
ub = int(input("Enter the upper bound: "))

display_range(lb, ub)


