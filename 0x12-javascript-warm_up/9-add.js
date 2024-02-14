#!/usr/bin/node
function add (a, b) {
  const c = a + b;
  console.log(c);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
