def countdown(i):
  print(i)
  if i <= 10:
    return
  else: 
    countdown(i - 1)

countdown(20)