def func3():
  return 3

def func2():
  return 2 + func3()

def func1():
  return 1 + func2()

x = func1()

