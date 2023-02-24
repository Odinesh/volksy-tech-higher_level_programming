#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];

function writeMe (file, content) {
  fs.writeFile(file, content, function (err) {
    if (err) {
      console.log(err);
    }
  });
}
writeMe(file, content);
