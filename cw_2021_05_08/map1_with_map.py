def square(num):
  return num ** 2

nums = [1,2,3,4,5]

squared = list(map(square, nums))

print("Original List:", nums)
print("Transformed List:", squared)


