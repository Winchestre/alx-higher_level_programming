#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2], 10);
function factorial (number) {
  if (number <= 1) { return number; }
  return number * factorial(number - 1);
}
console.log(`${isNaN(num) ? 1 : `${factorial(num)}`}`);
