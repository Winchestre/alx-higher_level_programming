#!/usr/bin/node
const { argv } = require('node:process');
const toNum = parseInt(argv[2], 10);
console.log(`${toNum ? `My number: ${toNum}` : 'Not a number'}`);
