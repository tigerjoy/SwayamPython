def pro_of_factor(num,f=1):
  if f>num//2:
    return(num)
  elif(num%f==0):
    return (f*pro_of_factor(num,f+1))
  else:
    return (pro_of_factor(num,f+1))
  
num=int(input("Enter a number:"))

print("Product of factors of", num ,"is",pro_of_factor(num))