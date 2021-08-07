# q9 (Page 99)

list1 = []

size = int(input("Enter the size of list: "))

print("Enter elements in the list")
for i in range(size):
  item = int(input("Enter element {}: ".format(i + 1)))
  list1.append(item)

dict_freq={}

for i in range(0,size):
  if list1[i] in dict_freq:
    dict_freq[list1[i]]=dict_freq[list1[i]]+1
  else:
    dict_freq[list1[i]]=1

item = -1
largest_freq=-1

for key,freq in dict_freq.items():
  if(freq>largest_freq):
    largest_freq=freq
    item=key

# Mode is 9 which has occurred 3 time(s)
print("Mode is",item,"which has occured",largest_freq,"times")