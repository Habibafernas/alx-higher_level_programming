#!/usr/bin/node
const fs = require('f');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
    console.log(error || content);
});
