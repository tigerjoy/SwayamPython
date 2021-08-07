list1 = []

size = int(input("Enter the size of list: "))

print("Enter elements in the list")
for i in range(size):
  item = int(input("Enter element {}: ".format(i + 1)))
  list1.append(item)

sum_even=0
sum_odd=0

for i in range(0,size):
  if(i%2==0):
    sum_even+=list1[i]
  else:
    sum_odd+=list1[i]

print(sum_even-sum_odd)
