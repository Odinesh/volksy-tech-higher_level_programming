#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
function concat (fileA, fileB, fileC) {
  fs.readFile(fileA, function (err, data) {
    if (err) {
      console.log(err.stack);
    }
    fs.appendFile(fileC, data);
  });
  fs.readFile(fileB, function (err, data) {
    if (err) {
      console.log(err.stack);
    }
    fs.appendFile(fileC, data);
  });
}
concat(fileA, fileB, fileC);
