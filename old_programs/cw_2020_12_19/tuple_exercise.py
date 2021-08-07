# Question 1

names=("Bobby","Hoshair","Ekta","Asta","Dave","Lily")

# Question 1 (a)

print(names[2:5])

# Question 1 (b)

tuple1=names[0:1]
print(tuple1)

# Question 1 (c)

print(names[3:6])

# Question 2

t1=("I am fine,thank you",)
t2=("How are you?",)
t3=t2+t1
print(t3)

#Question 3

'''
t=()
n=int(input("Enter size of the tuple:"))

for i in range(0,n):
  item=input("Enter element:")
  t=t+(item,)

t1 = ()
for i in range(0,n,3):
  t1=t1+(t[i],)
print(t1)
'''

#Question 4

'''
t=()
n=int(input("Enter size of the tuple:"))

for i in range(0,n):
  item=input("Enter element:")
  t=t+(item,)

i=0
while(i<n):
  print(t[i],end=",")
  i=i+2
'''


#Question 5
'''
t=()
n=int(input("Enter size of the tuple:"))

for i in range(0,n):
  item=int(input("Enter element:"))
  t=t+(item,)

i=0
while(i<n):
  print(t[i]**3,end=",")
  i=i+3

'''

#Question 6
'''
t=()
n=int(input("Enter size of the tuple:"))

for i in range(0,n):
  item=input("Enter element:").upper()
  t=t+(item,)

i=0
while(i<n):
  word=t[i]
  piglatin=word[1:]+word[0]+"AY"
  print(piglatin)
  i=i+1

'''

#Question 7

'''
IAY
WERTYQAY
SDFGHAAY
XCVBNZAY
OIUYTPAY
'''

# WERTYQAY -> Remove AY
# WERTYQ -> Bring the last letter to the first
# QWERTY
'''
t=()
n=int(input("Enter size of the tuple:"))

for i in range(0,n):
  item=input("Enter element:").upper()
  t=t+(item,)

i=0
while(i<n):
  piglatin=t[i]
  # Removing AY from the end
  piglatin=piglatin[0:-2]
  # Bring last letter to first
  word=piglatin[-1]+piglatin[0:-1]
  print(word)
  i=i+1

'''
#Question 8(a)

'''
pets = (
  ('Bruno', 4),
  ('Tommy', 3),
  ('Rainy', 2),
  ('Lucy', 5)
)
'''

# Dog Name: Bruno, Age: 4
'''
for dog_name,age in pets:
  print("Dog Name:",dog_name,"Age:",age)
'''

#Question 8 (b)
'''
for dog_name,age in pets:
  print("Age:",age)
'''

#Question 8 (c)

pets = (
  ('Bruno', 4, 'dog'),
  ('Tommy', 3, 'cat'),
  ('Rainy', 2, 'dog'),
  ('Lucy', 5, 'cat'),
  ('Mewmew', 3, 'cat'),
)

'''
count=0
for dog_name,age,species in pets:
  if(species=="dog"):
    count=count+1
print("Numbers of dogs are", count)
'''
#Question 8 (d)

'''
sum_age=0
for dog_name,age,species in pets:
  sum_age=sum_age+age
print("Sum of age of pets are", sum_age)
'''

#Question 8 (e)

'''
T=()
n=int(input("How many sub-tuples do you want to enter:"))
for i in range(0,n):
  tup1=eval(input("Enter a tuple:"))
  # () + ((1,2),) -> ((1,2))
  # () -> ((1,2)) 
  T=T+(tup1,)

# ((1,2), (1,2,3)) -> (2, 3)

len_tup=()
for subtuple in T:
  len_tup=len_tup+(len(subtuple),)
print(len_tup)
'''

# Question 8 (f)

T=()
n=int(input("How many sub-tuples do you want to enter:"))
for i in range(0,n):
  tup1=eval(input("Enter a tuple:"))
  T=T+(tup1,)

len_tuple=()
for subtuple in T:
  len_tuple=len_tuple+(len(subtuple),)

# Run the loop until no subtuples remain
while (len(T)!=0):
  # Find the minimum length
  min_len=min(len_tuple)
  # Find the index of the subtuple
  # having the minimum length
  index=len_tuple.index(min_len)
  # Display the subtuple having the
  # minimum length
  print(T[index],end=";")
  # Remove the current minimum length
  # subtuple from T
  T=T[0:index]+T[index+1:]
  len_tuple=len_tuple[0:index]+len_tuple[index+1:]
  


# Question 9

'''
n = int(input("Enter the value of n: "))

# n = 2
# (2, 4, 6, 8)

tup1 = (n, 2 * n, 3 * n, 4 * n)

print(tup1)
'''