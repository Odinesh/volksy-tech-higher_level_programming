#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let largest, second;
  if (parseInt(process.argv[2]) >= parseInt(process.argv[3])) {
    largest = parseInt(process.argv[2]);
    second = parseInt(process.argv[3]);
  } else {
    largest = parseInt(process.argv[3]);
    second = parseInt(process.argv[2]);
  }

  for (let i = 4; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > largest) {
      second = largest;
      largest = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > second) {
      second = parseInt(process.argv[i]);
    }
  }
  console.log(second);
}
