#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      const wdth = c.repeat(this.width);
      console.log(wdth);
    }
  }
};
