#!/usr/bin/node

/*
Prints the first argument passed
*/

const firstArg = process.argv[2];

if (process.argv[2]) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
