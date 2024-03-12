#!/usr/bin/node

function factorial(n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log(1); // Factorial of NaN is 1
} else {
  console.log(factorial(num));
}  
