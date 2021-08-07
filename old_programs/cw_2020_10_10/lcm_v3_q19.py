def lcm(num1,num2):
  count=1
  for i in range(1,num1*num2+1): 
    if(count%num1==0 and count%num2==0):
      break
    else:
      count=count+1
  return(count)

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
# Template
# "LCM(2, 4) = 4"
# Change the variable part to {}
# "LCM({}, {}) = {}"
# Using format()
# "LCM({}, {}) = {}".format(num1, num2, )

print("LCM({}, {}) = {}".format(num1, num2, lcm(num1,num2)))