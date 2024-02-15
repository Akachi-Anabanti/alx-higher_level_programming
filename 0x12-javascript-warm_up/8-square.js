#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] && parseInt(argv[2])) {
  const size = parseInt(argv[2]);
  for (let i = 0; i < size; i++) {
    const repeated = 'X'.repeat(size);
    console.log(repeated);
  }
} else {
  console.log('Missing size');
}
