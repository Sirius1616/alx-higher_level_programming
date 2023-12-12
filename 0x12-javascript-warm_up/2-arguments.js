#!/usr/bin/node
const myvar = process.argv.length;
console.log(myvar === 2 ? 'No argument' : myvar === 3 ? 'Argument found' : 'Arguments found');
