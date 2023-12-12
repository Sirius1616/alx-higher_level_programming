#!/usr/bin/node
const myvar = process.argv.length - 2;
console.log(myvar === 2 ? 'No argument' : myvar === 3 ? 'Argument found' : 'Arguments found');
