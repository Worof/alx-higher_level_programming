#!/usr/bin/node

// Import the dictionary from 101-data.js
const { dict } = require('./101-data.js');

const newDict = {};

// Iterate over each key-value pair in the original dictionary
for (const [userId, occurrence] of Object.entries(dict)) {
  // If the occurrence key doesn't exist in newDict, initialize it with an empty array
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }
  
  // Push the user ID to the corresponding occurrence key in newDict
  newDict[occurrence].push(userId);
}

// Print the new dictionary
console.log(newDict);
