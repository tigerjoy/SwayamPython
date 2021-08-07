def countdigits(string):
  count=0
  for ch in string:
    if(ch.isdigit()):
      count=count+1
  return(count)

def countvowel(string):
  count=0
  for ch in string:
    if(ch in "aeiouAEIOU"):
      count=count+1
  return(count)

def countconsonant(string):
  count=0
  for ch in string:
    if(ch not in "aeiouAEIOU" and ch.isalpha()):
      count=count+1
  return(count)

def countspecial(string):
  count=0
  for ch in string:
    if(not ch.isalnum()):
      count=count+1
  return(count)

string=input("Enter a sentence:")
print("No. of digits:",countdigits(string))
print("No. of vowels:",countvowel(string))
print("No. of consonants:",countconsonant(string))
print("No. of special characters:",countspecial(string))