#!/usr/bin/node

const { argv } = require('node:process');

function factorial (n) {
  if (n === 1 || isNaN(n) || n === 0) {
    return (1);
  }
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(argv[2])));
