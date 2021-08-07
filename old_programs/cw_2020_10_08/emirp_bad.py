n=int(input("Enter a number: "))

# Creating a copy of n
num = n

# To reverse n
rev=0
while(n!=0):
  dig=n%10
  rev=(rev*10)+dig
  n=n//10

# Counting the factors of num
count_num=0
for i in range(1,num+1):
  if(num%i==0):
    count_num=count_num+1

# Counting the factors of rev
count_rev=0
for i in range(1,rev+1):
  if(rev%i==0):
    count_rev=count_rev+1

if(count_num == 2 and count_rev == 2):
  print(num,"is an emrip number")
else:
  print(num,"is not an emrip number")  

