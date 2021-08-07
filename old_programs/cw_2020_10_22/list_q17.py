size=int(input("Enter size of a list:"))
arr=[]
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

largest=arr[0]
for i in range(1,size):
  if(arr[i]>largest):
    largest=arr[i]

smallest=arr[0]
for i in range(1,size):
  if(arr[i]<smallest):
    smallest=arr[i]
    
diff=largest-smallest    
print("Difference between largest and smallest element is:",diff)