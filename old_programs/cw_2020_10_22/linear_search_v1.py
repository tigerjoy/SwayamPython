def linear_search(arr,key):
  pos=None
  n= len(arr)
  for i in range(0,n):
    if(key==arr[i]):
      pos=i
      break
  return(pos)

size=int(input("Enter size of a list:"))
arr=[]
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

key=int(input("Enter the element to be searched:"))

pos=linear_search(arr,key)
if(pos==None):
  print(key,"has not been found.")
else:
  print(key,"has been found at position",pos)