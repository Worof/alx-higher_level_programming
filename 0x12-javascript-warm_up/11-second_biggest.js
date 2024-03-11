#!/usr/bin/node

function secondBiggest(arr) {
    if (arr.length < 2) {
      return 0;
    }
  
    // Convert arguments to integers
    const integers = arr.map(Number);
  
    // Sort the integers in descending order
    const sortedIntegers = integers.sort((a, b) => b - a);
  
    // Return the second largest integer
    return sortedIntegers[1];
  }
  
  const args = process.argv.slice(2);
  console.log(secondBiggest(args));
  