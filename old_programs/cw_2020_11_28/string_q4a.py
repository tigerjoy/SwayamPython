string=input("Enter a sentence:")
vowels=""
consonants=""

string=string.upper()

for ch in string:
  if(ch in "AEIOU"):
    vowels=vowels+ch
  elif(ch.isalpha()):
    consonants=consonants+ch

print("VOWEL WORD:",vowels)
print("CONSONANT WORD:",consonants)