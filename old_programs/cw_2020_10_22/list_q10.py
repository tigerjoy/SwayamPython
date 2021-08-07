size=int(input("Enter size of a list:"))
arr=[]
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

sum=0
pro=1
for i in range(0,size):
  if(arr[i]%2==1):
    sum=sum+arr[i]
  else:
    pro=pro*arr[i] 
    
print("sum is:",sum)
print("product is:",pro)

  