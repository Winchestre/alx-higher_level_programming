#!/usr/bin/node
const { argv } = require('node:process');
let x = parseInt(argv[2], 10);
if (!isNaN(x)) {
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
} else console.log('Missing number of occurrences');
