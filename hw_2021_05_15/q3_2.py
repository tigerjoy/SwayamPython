# COMMENTS BY Ranajoy:
"""
1. You should not name the function chr() because
   chr() is an inbuilt function of Python and 
   naming a function chr() would redefine chr() and
   the built in chr() would not be callable from this program.

2. This function should take two char arguments,
   hence the function should have two parameters and
   input should be taken from the __main__ part of
   the program.
"""

def chr() :
  char1 = input("Enter a Char 1 : ")
  char2 = input("Enter a Char 2 : ")
  if char1 == char2 :
    print("Ture")
  else:
    print("False ")

chr()