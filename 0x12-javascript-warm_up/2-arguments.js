#!/usr/bin/node
const myvar = process.argv.length - 2;
console.log(myvar === 1 ? 'No argument' : myvar === 2 ? 'Argument found' : 'Arguments found');
