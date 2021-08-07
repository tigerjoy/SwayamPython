def dec2bin(num):
  if(num==0):
    return("0")
  else:
    return(dec2bin(num//2)+str(num%2))
  
num=int(input("Enter a number:"))

# (5)10 = (0101)2
print("(", num ,")10 = (",dec2bin(num),")2")