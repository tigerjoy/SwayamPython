def marks_calc(**kwargs):
  total=0
  for subject,marks in kwargs.items():
    print(subject,"=",marks)
    total=marks+total
  avg=total/len(kwargs)
  print("total marks =",total,"out of",len(kwargs)*100)
  print("Avg marks=",avg)



marks = {'english':89,'computer':99,'maths':96}
marks_calc(**marks)

