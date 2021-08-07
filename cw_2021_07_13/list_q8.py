def sum_of_list(arr):
  if(len(arr)==0):
    return(0)
  else:
    return(arr[-1]+sum_of_list(arr[0:len(arr)-1]))
    

arr = eval(input("Enter the elements enclosed within []:")) 

print(sum_of_list(arr))