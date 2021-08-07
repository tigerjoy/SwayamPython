dict_users={}
for i in range(1,11):
  # Enter username of user 1: 
  username=input("Enter username of user {}:".format(i))
  password=input("Enter password of user {}:".format(i))
  dict_users[username]=password

print("Enter log in details:")
username=input("Enter username of user :")
password=input("Enter password of user :")

# If the username is present in the dictionary
if(username in dict_users):
  # If the entered password is of the username
  if(dict_users[username] == password):
    print("Welcome",username,"you are now logged in")
  else:
    print("Password is invalid")
else:
  print(username,"is not a valid user")

  
