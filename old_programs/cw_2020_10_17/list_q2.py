size=int(input("Enter the size of the list:"))
arr = []
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

# Using for-each loop
# for item in arr[::-1]:
#   print(item,end=",")

# Without using for-each loop
for i in range(-1,-size-1,-1):
  print(arr[i],end=",")