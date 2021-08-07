def fibo_itr(n):
  if(0<=n<=1):
    return n
  else:
    t1 = 0
    t2 = 1
    for i in range(n-1):
      t3 = t1 + t2
      t1 = t2
      t2 = t3
    return t3

memo = {}
def fibo_memo(n):
  if(n == 0):
    return 0
  elif(n == 1):
    return 1
  else:
    if(n in memo):
      return memo[n]
    else:
      memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
      return memo[n]

print(fibo_memo(50)) #12586269025