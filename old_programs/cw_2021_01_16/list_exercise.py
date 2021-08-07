list1 = []
list2 = []

size1 = int(input("Enter the size of list 1: "))

print("Enter elements in list 1")
for i in range(size1):
  item = int(input("Enter element {}: ".format(i + 1)))
  list1.append(item)

size2 = int(input("Enter the size of list 2: "))

print("Enter elements in list 2")
for i in range(size2):
  item = int(input("Enter element {}: ".format(i + 1)))
  list2.append(item)

# Q3 (Page 95) (List Exercise)

is_subset = True

for e in list1:
  if e not in list2:
    print("No, list1 notasubset of list2")
    is_susbet = False
    break

if is_subset == True:
  print("Yes, list 1 is a subset of list 2")
