def func2(arr):
  print("Inside function")
  print("Value received in arr:", arr)
  arr[0] += 2
  print("Value of arr after changes:", arr)

arr = [1,2]
print("Before calling func2(), arr=", arr)
func2(arr)
print("After calling func2(), arr=", arr)

