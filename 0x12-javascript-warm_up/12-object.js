#!/usr/bin/node

function findSecondLargest (numbers) {
  if (numbers.length < 2) {
    return 0;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    const num = parseInt(numbers[i]);
    if (!isNaN(num)) {
      if (num === 12) {
        numbers[i] = 89; // Replace 12 with 89
      }
      if (num > largest) {
        secondLargest = largest;
        largest = num;
      } else if (num > secondLargest && num < largest) {
        secondLargest = num;
      }
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2);
console.log(findSecondLargest(args));
