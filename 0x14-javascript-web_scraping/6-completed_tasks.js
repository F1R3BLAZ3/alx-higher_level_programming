#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);

    const completedTasksByUsers = {};
    
    for (const todo of todos) {
      const userId = todo.userId;
      const completed = todo.completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) {
        completedTasksByUsers[userId]++;
      }
    }

    console.log(completedTasksByUsers);
  } else {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
