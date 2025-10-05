# Binary search recursion algorithm

def binarySearch(arr, target, low, high):
  # base case
  if low > high:
    return ValueError("Target not in array")
  
  mid = (low + high) // 2
  guess = arr[mid]


  # base case
  if guess == target:
    return mid
  # recursive case
  elif guess < target:
    return binarySearch(arr, target, mid + 1, high)
  else:
    return binarySearch(arr, target, low, mid - 1)


sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binarySearch(sorted_list, 91, 0, len(sorted_list) - 1))