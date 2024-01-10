#!/usr/bin/node
const Square = class Square extends require('./5-square.js') {
  constructor (size) {
    super();
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.size; i++) {
        let y = '';
        for (let j = 0; j < this.size; j++) {
          y += 'X';
        }
        console.log(y);
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        let x = '';
        for (let j = 0; j < this.size; j++) {
          x += c;
        }
        console.log(x);
      }
    }
  }
};
module.exports = Square;
