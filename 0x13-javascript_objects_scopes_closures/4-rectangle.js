#!/usr/bin/node
const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i <= this.height - 1; i++) {
      let x = '';
      for (let j = 0; j <= this.width - 1; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  rotate () {
    let tmp = '';
    tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
module.exports = Rectangle;
