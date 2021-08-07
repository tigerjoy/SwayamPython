list1 = []

size = int(input("Enter the size of list: "))

print("Enter elements in the list")
for i in range(size):
  item = int(input("Enter element {}: ".format(i + 1)))
  list1.append(item)

# Initialized with an odd number
largest_even=1

for item in list1:
  if(item%2==0):
    if(item>largest_even or largest_even == 1):
      largest_even=item

if(largest_even==1):
  print("No even element")
else:
  print(largest_even)