#!/usr/bin/node

// Import the array from 100-data.js
const { list } = require('./100-data.js');

// Check if the list is imported correctly
console.log(list);

// Use map to create a new array
const newList = list.map((element, index) => element * index);

// Print the new list
console.log(newList);
