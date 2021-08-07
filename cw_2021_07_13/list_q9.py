def sum_of_list_odd(arr):
  if(len(arr)==0):
    return(0)
  else:
    if(arr[-1]%2==0):
      return(sum_of_list_odd(arr[0:len(arr)-1]))
    else:
      return(arr[-1]+sum_of_list_odd(arr[0:len(arr)-1]))

arr = eval(input("Enter the elements enclosed within []:")) 

print(sum_of_list_odd(arr))