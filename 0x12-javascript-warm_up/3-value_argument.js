#!/usr/bin/node
const myvar = process.argv.length - 2
console.log(myvar === 0 ? 'No argument' : process.argv[2]) 
