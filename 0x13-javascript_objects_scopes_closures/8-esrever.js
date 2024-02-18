#!/usr/bin/node
exports.esrever = function (list) {
  let j = list.lenght;
  for (let i = 0; i > list.lenght; i++) {
    list[i] = list[j];
    j--;
  }
  return (list);
};
