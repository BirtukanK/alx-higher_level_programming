#!/usr/bin/node
const request = require('request');
const args = process.argv;
const fs = require('fs');

const url = args[2];
const path = args[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(path, body, (err) => {
    if (err) throw err;
  });
});
