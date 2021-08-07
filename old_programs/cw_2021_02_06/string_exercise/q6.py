word=input("Enter a word: ")

print("The letters of the word are")
for i in range(len(word)):
  print(word[i], end=",")

print("\nThe letters of the word in reverse are")
for i in range(len(word)-1, -1, -1):
  print(word[i],end=",")

rev_word=word[::-1]
print("\nThe reverse word is:",rev_word)

letter=input("Enter a letter: ")
count=0
for i in range(0,len(word)):
  if(word[i]==letter):
    count=count+1

print("Letter",letter,"occured",count,"times.")