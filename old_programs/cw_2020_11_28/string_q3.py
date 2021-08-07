def countupper(string):
  count=0
  for ch in string:
    if(ch.isupper()):
      count=count+1
  return(count)

def countlower(string):
  count=0
  for ch in string:
    if(ch.islower()):
      count=count+1
  return(count)

def countdigits(string):
  count=0
  for ch in string:
    if(ch.isdigit()):
      count=count+1
  return(count)

string=input("Enter a sentence:")
print("No. of uppercase character:",countupper(string))
print("No. of lowercase character:",countlower(string))
print("No. of digits:",countdigits(string))