def iseven(num):
  return(num%2==0)

def isodd(num):
  return(num%2==1)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19]

even = list(filter(iseven, nums)) 
odd = list(filter(isodd, nums))

print("Original List:", nums)
print("Filtered Even List:", even)
print("Filtered Odd List:", odd)

