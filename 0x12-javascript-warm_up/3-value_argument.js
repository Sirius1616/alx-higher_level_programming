#!/usr/bin/node

const arg = process.argv;

let count = 0;
for (const item in arg){
	count++;
}

if (count === 2){
	console.log('No argument');
}	else {
	console.log(arg[2]);
}
