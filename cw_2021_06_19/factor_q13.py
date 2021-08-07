def display_factors(num,f=1):
  if f>num//2:
    print(num)
    return
  elif(num%f==0):
    print(f)
    display_factors(num,f+1)
  else:
    display_factors(num,f+1)
  
num=int(input("Enter a number:"))

display_factors(num)