n=int(input("Enter the number of terms:"))

prev_t=1
s=1
for i in range(2,n+1):
  curr_t=prev_t*10+1
  s=s+curr_t
  prev_t=curr_t
  
print("The sum of the series is:",s)