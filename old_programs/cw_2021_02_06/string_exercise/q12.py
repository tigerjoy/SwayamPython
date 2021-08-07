word=input("Enter a word:")

if(word[0].isnumeric() and len(word)>=6):
  print("Password is accepted.")
else:
  print("Password is not valid.")