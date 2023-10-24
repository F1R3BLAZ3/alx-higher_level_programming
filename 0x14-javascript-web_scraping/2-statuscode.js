#!/usr/bin/node

const https = require('https');

const url = process.argv[2];

https.get(url, (response) => {
  console.log(`code: ${response.statusCode}`);
})
.on('error', (error) => {
  console.error(error);
});
