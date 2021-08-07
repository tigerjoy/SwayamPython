string=input("Enter a sentence:")
# revstr=""
# for word in string.split()[::-1]:
#   revstr=revstr+word+" "
revstr = " ".join(string.split()[::-1])

print("Reversed word is:", revstr)

