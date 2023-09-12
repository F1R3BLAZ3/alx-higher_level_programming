#!/usr/bin/node

const BaseSquare = require('./5-square'); // Import the Square class from 5-square.js

class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
