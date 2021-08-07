nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19]

even = list(filter(lambda num:num%2==0, nums)) 
odd = list(filter(lambda num:num%2==1, nums))

print("Original List:", nums)
print("Filtered Even List:", even)
print("Filtered Odd List:", odd)

