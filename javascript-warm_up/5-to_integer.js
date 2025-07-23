#!/usr/bin/node

/*
prints My number: <first argument converted in integer>
*/

const firstArg = process.argv[2];

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(firstArg)}`);
}
