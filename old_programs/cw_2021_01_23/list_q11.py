# q11 (page 100)

list1 = []

size = int(input("Enter the size of list: "))

print("Enter elements in the list")
for i in range(size):
  item = int(input("Enter element {}: ".format(i + 1)))
  list1.append(item)

list2=[list1[0]] #length = 1, #valid_index = 0

for i in range(1,size):
  list2.append(list2[i-1]+list1[i])

print("Original list\n",list1)
print("Cumulative sum list\n",list2)