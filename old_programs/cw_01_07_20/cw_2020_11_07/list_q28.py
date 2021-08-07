size=int(input("Enter size of the list:"))
arr=[]
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

visited=[]
for i in range(0,size):
  if arr[i] not in visited:
    count=arr.count(arr[i])
    print(arr[i],"occurs",count,"times")
    visited.append(arr[i])