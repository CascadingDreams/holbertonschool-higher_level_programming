#!/usr/bin/node

const numberofTimes = process.argv[2];
const square = 'X';

if (isNaN(numberofTimes)) {
  console.log('Missing size');
}
for (let i = 0; i < numberofTimes; i++) {
  console.log(square.repeat(numberofTimes));
}
