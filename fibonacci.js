const memo = {};

function fib(n){
  // check if the result is already in memo
  if(n in memo){
    return memo[n];
  }

  // base cases for fibonacci sequence
  if(n <= 1){
    return n;
  }

  // if not in cache, compute the result
  const result = fib(n - 1) + fib(n - 2);
  memo[n] = result;

  // Return the result
  return result;
}

console.time("Fibonacci")
console.log(`The 10th Fibonacci number is ${fib(8)}`)
console.timeEnd("Fibonacci")