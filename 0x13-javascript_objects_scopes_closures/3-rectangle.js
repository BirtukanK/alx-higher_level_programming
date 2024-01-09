#!/usr/bin/node
const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i <= this.width; i++) {
      for (let j = 0; j <= this.height; j++) {
        console.log('X');
	console.log('\n');
      }
      console.log('\n');
    }
  }
};
module.exports = Rectangle;
