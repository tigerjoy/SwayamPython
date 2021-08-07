size=int(input("Enter the size of the list:"))
arr = []
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

for item in arr:
  if not (item == 7 or item == 9):
    print(item,end=",")

# When we should display
# not (item == 7 or item == 9)
# item != 7 and item != 9

# When we should not display
# item == 7 or item == 9

