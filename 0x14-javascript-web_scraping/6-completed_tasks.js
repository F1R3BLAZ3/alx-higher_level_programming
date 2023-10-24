#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, _res, body) => {
  if (err) {
    console.error(err);
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) {
        ++completedTasksByUsers[userId];
      }
    }

    console.log(JSON.stringify(completedTasksByUsers, null, 2));
  }
});
