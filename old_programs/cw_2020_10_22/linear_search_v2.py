def linear_search(arr,key):
  pos=None
  n= len(arr)
  for i in range(0,n):
    if(key==arr[i]):
      print(key,"has been found in position",i)
      pos=i
  if(pos==None):
    print(key,"was not found.")

size=int(input("Enter size of a list:"))
arr=[]
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

key=int(input("Enter the element to be searched:"))

linear_search(arr,key)
