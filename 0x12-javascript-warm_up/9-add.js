#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (isNaN(arg1) || isNaN(arg2)) {
  console.log('Invalid input. Please provide two integers as arguments.');
} else {
  add(arg1, arg2);
}
