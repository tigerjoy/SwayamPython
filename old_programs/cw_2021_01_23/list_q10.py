# q10 (Page 99)

list1 = []

size = int(input("Enter the size of list: "))

print("Enter elements in the list")
for i in range(size):
  item = int(input("Enter element {}: ".format(i + 1)))
  list1.append(item)

print("Range is",max(list1)-min(list1))