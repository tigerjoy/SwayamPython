def func1():
  print("Start of func1()")
  return 
  print("End of func1()")

def func2():
  print("Start of func2()")
  func1()
  print("End of func2()")

func2()


