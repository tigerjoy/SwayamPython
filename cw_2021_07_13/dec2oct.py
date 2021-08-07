def dec2oct(num):
  if(num==0):
    return("0")
  else:
    return(dec2oct(num//8)+str(num%8))
  
num=int(input("Enter a number:"))

# (8)10 = (10)8
print("(", num ,")10 = (",dec2oct(num),")8")