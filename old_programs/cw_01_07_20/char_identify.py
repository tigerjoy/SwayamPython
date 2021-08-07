ch = input("enter a character: ")

if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
  print("the character is a letter")
  if (ch>='A' and ch<='Z'):
    print("The character is a uppercase letter")
  else:
    print("The character is a lowercase letter")
elif (ch>='0' and ch<='9'):
  print("The character is a digit")
else:
  print("The character is a special character")
