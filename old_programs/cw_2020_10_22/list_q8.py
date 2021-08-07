size=int(input("Enter size of a list:"))
arr=[]
for i in range(0,size):
  item=int(input("Enter element {}:".format(i+1)))
  arr.append(item)

sum=0
for i in range(0,size):
  sum=sum+arr[i]
    
print("sum is:",sum)
  