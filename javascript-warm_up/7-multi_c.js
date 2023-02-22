#!/usr/bin/node
const n = Number.parseInt(process.argv[2]);
if (n > 0) {
  let i;
  for (i = 0; i < n; i++) {
    console.log('C is fun');
  }
} else if (isNaN(n)) {
  console.log('Missing number of occurrences');
}
