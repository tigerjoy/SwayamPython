def func3(arr):
  print("Inside function")
  print("Value received in arr:", arr)
  arr.pop()
  arr.append(6)
  print("Value of arr after changes:", arr)

arr = [1,2]
print("Before calling func2(), arr=", arr)
func3(arr)
print("After calling func2(), arr=", arr)

