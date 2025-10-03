memo = {}

def fib(n):
  if(n in memo):
    return memo[n]
  
  if(n <= 1):
    return n
  
  result = fib(n - 1) + fib(n - 2)
  memo[n] = result

  return result

print("The Fibonacci output for " + str(fib(8)))