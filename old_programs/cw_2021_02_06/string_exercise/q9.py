word1=input("Enter a word:")
word2=input("Enter another word:")

if word1.startswith(word2):
  print(word2,"is a prefix of",word1)
elif word2.startswith(word1):
  print(word1,"is a prefix of",word2)
else:
  print("Neither is a prefix of the other")