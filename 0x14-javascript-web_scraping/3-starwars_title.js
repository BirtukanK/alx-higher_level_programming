#!/usr/bin/node
const request = require('request');

const args = process.argv;
const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + args[2];

request(endpoint, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
