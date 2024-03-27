#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + process.argv[2], function (err, request, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    request.get(i, function (err, request, body1) {
      if (err) {
        console.log(err);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
