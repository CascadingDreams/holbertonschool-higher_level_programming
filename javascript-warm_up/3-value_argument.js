#!/usr/bin/node

/*
Prints the first argument passed
*/

const firstArg = process.argv[3];

if (process.argv[3]) {
    console.log(firstArg);
} else {
    console.log('No argument');
}
