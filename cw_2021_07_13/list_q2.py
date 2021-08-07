def displayrev(arr):
  if(len(arr)==0):
    print()
  else:
    print(arr[-1],end=",")
    displayrev(arr[0:len(arr)-1])
  
arr = eval(input("Enter the elements enclosed within []:")) 
print(type(arr))
displayrev(arr)
