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
  print(item + "INSERTED INTO STACK")

def pop():
  global top, STACK
  # Check for underflow
  # if top is None:
  if is_empty():
    print("STACK UNDERFLOW")
    return None
  else:
    ret_val = STACK[top]
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


# __main__
# Initial state of STACK
STACK = []
top = None