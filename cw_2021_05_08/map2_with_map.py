names = ["ranajoy", "Swayam", "arnab", "arka", "Tamoghna"]

def capitalize(word):
  return(word[0].upper()+word[1:])

capitalized=list(map(capitalize,names))

print("Original List: ", names)
print("Transformed List: ", capitalized)
