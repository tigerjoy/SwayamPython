def sum_of_factor(num,f=1):
  if f>num//2:
    return(num)
  elif(num%f==0):
    return (f+sum_of_factor(num,f+1))
  else:
    return (sum_of_factor(num,f+1))
  
num=int(input("Enter a number:"))

print("Sum of factors of", num ,"is",sum_of_factor(num))