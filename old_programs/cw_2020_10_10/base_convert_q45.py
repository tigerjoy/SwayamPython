def dec_to_bin(n):
  bin=""
  while(n!=0):
    rem=n%2
    bin=str(rem)+bin
    n=n//2
  return(bin)

def dec_to_oct(n):
  oct=""
  while(n!=0):
    rem=n%8
    oct=str(rem)+oct
    n=n//8
  return(oct)

def dec_to_hex(n):
  hex=""
  while(n!=0):
    rem=n%16
    if rem < 10:
      hex=str(rem)+hex
    else:
      hex=chr(rem + 55)+hex
    n=n//16
  return(hex)

# (5)10 = (101)2
# (5)10 = (5)8
# (5)10 = (5)16


n=int(input("Enter a number:"))
print("({})10 = ({})2".format(n,dec_to_bin(n)))
print("({})10 = ({})8".format(n,dec_to_oct(n)))
print("({})10 = ({})16".format(n,dec_to_hex(n)))
