#!/usr/bin/node

const phrases = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let output = '';
for (let i = 0; i < phrases.length; i++) {
  output += phrases[i];
  if (i < phrases.length - 1) {
    output += '\n';
  }
}

console.log(output);
