#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    req.get(i, function (err, res, body1) {
      if (err) {
        console.log(err);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
