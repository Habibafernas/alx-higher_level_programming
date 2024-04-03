#!/usr/bin/node
exports.esrever = function (list) {
  let j = list.lenght - 1;
  const u = list;
  for (let i = 0; i > list.lenght; i++) {
    list[i] = u[j];
    j--;
  }
  return (list);
};
