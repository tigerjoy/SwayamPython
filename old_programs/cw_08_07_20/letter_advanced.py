import string

char=input("Enter a letter: ")

if char in "aeiouAEIOU":
  print('it is a vowel')
elif char in string.ascii_letters:
  print('it is a consonant')
else:
  print('it is not a letter')
