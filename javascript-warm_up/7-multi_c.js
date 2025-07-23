#!/usr/bin/node

const numberofTimes = process.argv[2];
const whatisFun = 'C is fun';

if (isNaN(numberofTimes)) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < numberofTimes; i++) {
  console.log(whatisFun);
}
