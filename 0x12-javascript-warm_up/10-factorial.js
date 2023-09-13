#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative number is 1
  }
  if (n === 0) {
    return 1; // Factorial of 0 is 1
  }
  return n * factorial(n - 1);
}

const input = parseInt(process.argv[2]);

console.log(factorial(input));
