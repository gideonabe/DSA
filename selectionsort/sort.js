function findSmallest(arr){
  // store the smallest element
  let smallest = arr[0];

  // store the index of the smallest el
  let smallest_index = 0;

  for(let i = 1; i < arr.length; i++){
    if(arr[i] < smallest){
      smallest = arr[i];
      smallest_index = i;
    }
  }

  return smallest_index;
}

// SELECTION SORT
function selectionSort(arr){
  let newArr = [];

  while(arr.length > 0){
    let smallest = findSmallest(arr);
    newArr.push(arr.splice(smallest, 1)[0]);
  }

  return newArr
}

// Measure execution time
console.time("SelectionSortTime"); // Start the timer
let test = selectionSort([5, 3, 6, 2, 10]);
console.timeEnd("SelectionSortTime"); // End the timer and log the time

console.log(test);
console.log(findSmallest(test));