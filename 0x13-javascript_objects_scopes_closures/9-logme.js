#!/usr/bin/node

let count = 0; // Initialize a counter to keep track of the number of arguments printed

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++; // Increment the counter after printing each argument
};
