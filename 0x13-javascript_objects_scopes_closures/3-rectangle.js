#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      Object.create(null);
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      const row = 'X'.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
}

module.exports = Rectangle;
