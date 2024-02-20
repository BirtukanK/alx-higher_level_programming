#!/usr/bin/node
const request = require('request');

const args = process.argv;
const endpoint = 'https://swapi-api.alx-tools.com/api/people/18/';

request(args[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const filmdata = JSON.parse(body);
  const moviesBy18 = filmdata.results.filter(film =>
    film.characters.includes(endpoint));
  console.log(moviesBy18.length);
});
