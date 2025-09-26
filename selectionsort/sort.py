def findSmallest(arr):
  # stores the smallest value
  smallest = arr[0]

  # stores the index of the smallest value
  smallest_index = 0

  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

#  SELECTION SORT 
def selectionSort(arr):
  newArr = []

  for i in range(len(arr)):
    # find the smallest element in the array and add it to the new array
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest))
  return newArr


test = selectionSort([5, 3, 6, 2, 10])
print(test)
print(findSmallest(test))