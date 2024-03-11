#!/usr/bin/node

const arg = process.argv[2];

const num = parseInt(arg);

if (!NaN(num)) {
    console.log(`My number is: {num}`);

} else {
    console.log("Not a number");
}