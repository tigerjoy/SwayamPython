def display_digits(n):
  if(0<=n<=9):
    print(n)                     
  else:
    print(n%10)
    display_digits(n//10)    

def display_digits_alt(n):
  if(0<=n<=9):
    print(n)                     
  else:
    display_digits_alt(n//10) 
    print(n%10)

print("Calling display_digits(1796)")
display_digits(1796)
print("Calling display_digits_alt(1796)")
display_digits_alt(1796)