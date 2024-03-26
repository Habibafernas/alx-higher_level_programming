#!/usr/bin/node
const f = require('f');
f.readFile(process.argv[2], 'utf8', function (error, content) {
    console.log(error || content);
});
