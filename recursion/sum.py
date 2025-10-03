# Array recursion

def sum(el):
  if not el:
    return 0
  else:
    return el[0] + sum(el[1:])
  
list=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

total = sum(list)
print(total)


# Count number of items in a list
def total(el):
  if not el:
    return 0  
  else: 
    return 1 + total(el[1:])
  
print(total(list))

# Maximum no in a list
def findmax(el):
  if not el:
    return ValueError("Empty list")
  if len(el) == 1:
    return el[0]
  else:
    firstEl = el[0]
    maxRemEl = findmax(el[1:])
  return max(firstEl, maxRemEl)

print(findmax(list))