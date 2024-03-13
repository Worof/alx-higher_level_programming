#!/usr/bin/node

let count = 0;  // This variable is private to the exported function below

exports.logMe = function (item) {
    console.log(`${count}: ${item}`);
    count++;  // Increase the count after logging
};
