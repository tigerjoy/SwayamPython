s=input("Enter a word:")
c=input("Enter a letter:")
output=""

for i in s.lower():
  if(i==c.lower()):
    output=output+i.upper()
  else:
    output=output+i

print(output)