#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(arg => parseInt(arg, 10));

  const uniqueNumbers = [...new Set(numbers)].sort((a, b) => b - a);

  if (uniqueNumbers.length >= 2) {
    console.log(uniqueNumbers[1]);
  } else {
    console.log(0);
  }
}
