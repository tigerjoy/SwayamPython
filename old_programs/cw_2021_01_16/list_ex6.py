list1 = []

size = int(input("Enter the size of list: "))

print("Enter elements in the list")
for i in range(size):
  item = int(input("Enter element {}: ".format(i + 1)))
  list1.append(item)
  
string1=""

for item in list1:
  string1=string1 + str(item)+"-"

print(string1[0:len(string1)-1])

#Alternate

# string1 = str(list1[0])

# for i in range(1,size):
#   string1 += "-" + str(list1[i])

# print(string1)