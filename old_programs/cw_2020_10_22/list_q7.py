size=int(input("Enter size of a list:"))
arr=[]
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

for i in range(0,size):
  if(arr[i]>10):
    print(arr[i],end=",")
  