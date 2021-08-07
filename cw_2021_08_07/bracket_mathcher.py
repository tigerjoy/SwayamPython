def push(item):
  global top, STACK
  # We are inserting for the first time
  # Hence, set top to 0
  # if top is None:
  if is_empty():
    top = 0
  # When inserting elements from second time
  # onwards, we increment top by 1
  else:
    top += 1
  STACK.append(item)
  print(item , "INSERTED INTO STACK")

def pop():
  global top, STACK
  # Check for underflow
  # if top is None:
  if is_empty():
    print("STACK UNDERFLOW")
    return None
  else:
    ret_val = STACK.pop()
    if top != 0:
      top = top - 1
    else:
      top = None
    return ret_val

def display():
  for i in range(top, -1, -1):
    print(STACK[i])

def is_empty():
  return top is None

def peek():
  if not is_empty():
    return STACK[top]
  else:
    return None

def is_bracket(ch):
  return ch in ("(",")","{","}","[","]")

def is_left_bracket(ch):
  # return(ch=="(" or ch=="{" or ch=="[")
  return ch in ("(", "{", "[")

def is_right_bracket(ch):
  return ch in (")", "}", "]")
  
def is_pair(ch1, ch2):
  return ((ch1=="(" and ch2==")") or 
          (ch1=="{" and ch2=="}") or 
          (ch1=="[" and ch2=="]"))
    
# __main__
# Initial state of STACK
STACK = []
top = None

is_matched = True
expression=input("Enter an expression:")
for ch in expression:
  if(is_bracket(ch)):
    if(is_left_bracket(ch)):
      push(ch)
    elif(is_right_bracket(ch)):
      top_bracket=pop() 
      # Case 3
      if top_bracket is None:
        print("Excess",ch)
        is_matched = False
        break
      # Case 1
      elif not is_pair(top_bracket,ch):
        print(top_bracket,"does not match with",ch)
        is_matched = False
        break

# Case 2
if(is_matched and not is_empty()):
  is_matched = False
  print("Excess")
  display()

if is_matched:
  print(expression, "contains matched parenthesis")