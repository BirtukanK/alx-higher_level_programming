#!/usr/bin/node
exports.esrever = function (list) {
  const toprint = [];
  for (let i = list.length - 1; i >= 0; i--) {
    toprint.push(list[i]);
  }
  return toprint;
};
