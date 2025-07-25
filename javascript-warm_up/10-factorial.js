#!/usr/bin/node

/* prints factorial of first arg */

const n = parseInt(process.argv[2]);

function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (isNaN(n)) {
  console.log('1');
} else {
  console.log(factorial(n));
}
