size=int(input("Enter the size of the list:"))
arr = []
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

for item in arr:
  if(item > 10):
    print(item**2,end=",")
