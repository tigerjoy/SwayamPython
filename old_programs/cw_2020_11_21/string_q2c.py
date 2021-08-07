def count(string,char):
  count=0
  for ch in string:
    if(ch==char):
      count=count+1
  return(count)      

# INPUT
string=input("Enter a word: ")
char=input("Enter the character to serarch for: ")
# OUTPUT
# ch occured 2 time(s) in str
# ch is not present in str
count=count(string,char)
if(count==0):
  print(char,"is not present in",string)
else:
  print(char,"occured",count,"times in",string)