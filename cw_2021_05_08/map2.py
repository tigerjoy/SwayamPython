names = ["ranajoy", "Swayam", "arnab", "arka", "Tamoghna"]
# Stores the capitalized strings of items in names
capitalized = []
#Do not change the above lines

# Code goes here
for i in names:
  new_name = i[0].upper()+i[1:]
  capitalized.append(new_name)

# Do not change the below lines
print("Original List: ", names)
print("Transformed List: ", capitalized)