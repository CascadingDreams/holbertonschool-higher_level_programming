#!/usr/bin/node

/*
prints two arguments passed to it, in the following format: “ is ”
*/

const firstArg = process.argv[2];
const secondArg = process.argv[3];
const result = `${firstArg} is ${secondArg}`;
console.log(result);
