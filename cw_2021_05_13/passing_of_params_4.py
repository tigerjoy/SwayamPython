def func4(arr):
  print("Inside function")
  print("Value received in arr:", arr)
  new_list = [5,6]
  arr = new_list
  print("Value of arr after changes:", arr)

arr = [1,2]
print("Before calling func2(), arr=", arr)
func4(arr)
print("After calling func2(), arr=", arr)

