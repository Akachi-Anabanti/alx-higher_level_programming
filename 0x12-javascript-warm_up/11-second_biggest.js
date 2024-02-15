#!/usr/bin/node

const { argv } = require('node:process');

function getSecondBiggest (argv) {
  if (isNaN(argv[2]) || parseInt(argv[2]) === 1) {
    return 0;
  }

  const arr = [];
  for (let i = 2; i < argv.length; i++) {
    // adds element to the array
    arr.push(parseInt(argv[i]));
  }
  // sorts it in decending order
  // using a comparison operation
  arr.sort(function (a, b) { return b - a; });
  return (arr[1]);
}
console.log(getSecondBiggest(argv));
