# q6 Answer (Page 97)

list1 = []

size = int(input("Enter the size of list: "))

print("Enter elements in the list")
for i in range(size):
  item = input("Enter element {}: ".format(i + 1))
  list1.append(item)

new_str=list1[0]

for i in range(1,size):
  new_str=new_str +"-" + list1[i]

print(new_str)