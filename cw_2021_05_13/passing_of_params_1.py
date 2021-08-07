def func1(s):
  print("Inside func1()")
  print("Value recieved in s:", s)
  s = 'A' + s[1:]
  print("Value of s changed to:", s)
  print("Returning...")

#__main__
s = "DAG"
print("Before calling func1(): s=", s)
func1(s)
print("After caling func1(): s =", s)

