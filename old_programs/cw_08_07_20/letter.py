char=input("Enter a letter: ")
char=char.lower()
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
  print('it is a vowel')
elif char>='a' and char<='z':
  print('it is a consonant')
else:
  print('it is not a letter')