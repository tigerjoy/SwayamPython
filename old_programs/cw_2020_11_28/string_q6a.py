string=input("Enter a sentence:")

print("{:10} {}".format("WORD", "LENGTH"))
for word in string.split():
  print("{:10} {}".format(word, len(word)))