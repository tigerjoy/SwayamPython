def list_input(arr,size):
  for i in range(0,size):
    item=int(input("Enter element {}:".format(i+1)))
    arr.append(item)

def list_display(arr):
  n=len(arr)
  for i in range(0,n):
    print(arr[i],end=",")
  print()

size1=int(input("Enter size of list 1:"))
arr1=[]
list_input(arr1,size1)

size2=int(input("Enter size of list 2:"))
arr2=[]
list_input(arr2,size2)

merge=arr1+arr2
print("Elements of list 1 are:")
list_display(arr1)

print("Elements of list 2 are:")
list_display(arr2)

print("Elements of merged list are:")
list_display(merge)







