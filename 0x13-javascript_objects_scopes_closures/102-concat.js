#!/usr/bin/node

const fs = require('fs');

// Get file paths from command-line arguments
const [,, fileA, fileB, fileC] = process.argv;

// Read and concatenate the contents of fileA and fileB
const contentA = fs.readFileSync(fileA, { encoding: 'utf8', flag: 'r' });
const contentB = fs.readFileSync(fileB, { encoding: 'utf8', flag: 'r' });
const contentC = contentA + contentB;

// Write the concatenated content to fileC
fs.writeFileSync(fileC, contentC);
