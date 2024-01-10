#!/usr/bin/node
exports.esrever = function (list) {
  let to_print = [];
  for (let i = list.length - 1; i >= 0; i--) {
    to_print.push(list[i]);
  }
  return to_print;
}
