# q8 answer (Page 98)

list1 = []

size = int(input("Enter the size of list: "))

print("Enter elements in the list")
for i in range(size):
  item = int(input("Enter element {}: ".format(i + 1)))
  list1.append(item)

list1.sort()

half=size//2

if (size%2==1):
  print(list1[half])
else:
  print((list1[half]+list1[half-1])/2)