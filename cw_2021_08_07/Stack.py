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

def display_menu():
  # TODO: Display the menu items
  print("Menu\n")
  print("Enter 1 to push an item into the stack\n")
  print("Enter 2 to pop an item out of the stack\n")
  print("Enter 3 to display items of the stack\n")
  print("Enter 4 to check stack status\n")
  print("Enter 5 to display top of the stack\n")
  print("Enter 6 to quit\n")


# __main__
# Initial state of STACK
STACK = []
top = None

# TODO: Run an infinite loop, display
# menu options to the user, do the appropriate
# task
while True:
  display_menu()
  choice=int(input("Enter choice(1-6): "))
  if(choice==6):
    print("Quitting...")
    break
  elif(choice==1):
    item=int(input("Enter the item to be pushed:"))
    push(item)
  elif(choice==2):
    item=pop()
    if(item is None):
      print("No item was deleted")
    else:
      print(item, "was deleted")
  elif(choice==3):
    print("The items in the stack are:")
    display()
  elif(choice==4):    
    print("The stack is empty" if(is_empty()) else "The stack is not empty")
  elif(choice==5):
    item=peek()
    if(item is None):
      print("The stack is empty")
    else:
      print("The top of the stack is",item)
  else:
    print("Invalid choice.")