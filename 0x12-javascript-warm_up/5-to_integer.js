#!/usr/bin/node
const myvar = Number(process.argv[2]);
console.log(('My number: ' + myvar !== isNaN(myvar)) ? myvar : 'Not a number')
