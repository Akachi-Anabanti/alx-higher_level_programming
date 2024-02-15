#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] && parseInt(argv[2])) {
  const occurence = parseInt(argv[2]);
  for (let i = 0; i < occurence; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
