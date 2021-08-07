name = input("Enter name of the student: ")
marks = float(input("Enter average marks of the student: "))

print("Name :",name)
if (marks>=80):
  print("Grade : Distinction")
elif (marks>=60 and marks < 80):
  print("Grade : First division")
elif (marks>=45 and marks < 60):
  print("Grade : Second division")
elif (marks>=40 and marks < 45):
  print("Grade : Pass")
else :
  print("Grade : Fail")

