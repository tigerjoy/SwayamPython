nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19]
# even stores the even numbers
even = []
# odd stores the odd numbers
odd = []
# Do not change the above lines

for i in nums:
  if(i%2==0):
    even.append(i)
  else:
    odd.append(i)


# Do not change the below lines
print("Original List:", nums)
print("Filtered Even List:", even)
print("Filtered Odd List:", odd)
