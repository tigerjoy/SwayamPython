total=0
count=0
avg=0

while (True):
  print("Enter -1 to stop")
  marks=int(input("Enter marks:"))
  if(marks==-1):
    break
  total=total+marks
  count=count+1
  avg=total/count
  print("Total marks:",total)
  print("Avg marks:",avg)
  print() 

print("Final Total marks:",total)
print("Final Avg marks:",avg)