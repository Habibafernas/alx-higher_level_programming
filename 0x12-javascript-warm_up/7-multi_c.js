#!/usr/bin/node
if (parseInt(process.argv[2])) {
  const x = parseInt(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
