def lcm(a,b,count=1):
  if(count%a==0 and count%b==0):
    return(count)
  else:
    return(lcm(a,b,count+1))
  
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))

print("LCM of", num1 ,"and",num2 ,"is:",lcm(num1,num2))