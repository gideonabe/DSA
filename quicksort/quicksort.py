def quicksort(arr):
  # basecase
  if len(arr) < 2:
    return arr
  
  # recursive case
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
  
print(quicksort([10 , 5, 2, 3]))

# Multiplication table with all the elements in the array
def create_multiplication_table(arr):
    multiplication_table = []
    for num1 in arr:
        row = []
        for num2 in arr:
            row.append(num1 * num2)
        multiplication_table.append(row)
    return multiplication_table

my_array = [1, 2, 3, 4, 5]
table = create_multiplication_table(my_array)
for r in table:
    print(r)
print(table)