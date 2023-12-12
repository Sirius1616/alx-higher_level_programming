#!/usr/bin/node
const myvar = process.argv.length - 2;
console.log(myvar === 0 ? 'No argument' : myvar === 1 ? 'Argument found' : 'Arguments found');
