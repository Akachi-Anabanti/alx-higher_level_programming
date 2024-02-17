#!/usr/bin/node

const BaseSquare = require('./5-square');
module.exports = class Square extends BaseSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      const wdth = c.repeat(this.width);
      console.log(wdth);
    }
  }
};
