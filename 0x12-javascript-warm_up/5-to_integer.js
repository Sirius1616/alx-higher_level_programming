#!/usr/bin/node
const myvar = Number(process.argv[2]);
console.log(!isNaN(myvar) ? `My number: ${myvar}` : 'Not a number');
