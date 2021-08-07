n=int(input("Enter the number of terms:"))

prev_t=2
s=2
for i in range(2,n+1):
  curr_t=prev_t+(2*i)
  s=s+curr_t
  prev_t=curr_t
  
print("The sum of the series is:",s)