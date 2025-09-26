def binary_search(list, item):
  # to keep track of which part of the list to search in
  low = 0
  high = len(list) - 1

  # while still narrowing down to one element
  while low <= high:
    # middle index
    mid = (low + high) // 2
    guess = list[mid]

    if guess == item:
      return mid
    if guess > item:
      # guess is too high
      high = mid - 1
    else:
      # guess is too low
      low = mid + 1

  # when item doesn't exist
  return None


my_list = [1, 3, 5, 7, 9, 10] 

print(binary_search(my_list, 10))
