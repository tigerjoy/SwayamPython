def dec2hex(num):
  remainder = num%16
  if(num==0):
    return("0")
  elif(remainder>=10):
    return(dec2hex(num//16)+chr(remainder+55))
  else:
    return(dec2hex(num//16)+str(remainder))
  
num=int(input("Enter a number:"))

# (1998)10 = (07CE)166
print("(", num ,")10 = (",dec2hex(num),")16")