#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksCount = {};

    for (const todo of todos) {
      if (todo.completed) {
        // Increment the completed task count for the user
        if (completedTasksCount[todo.userId]) {
          completedTasksCount[todo.userId]++;
        } else {
          completedTasksCount[todo.userId] = 1;
        }
      }
    }

    // Print the results in the expected format
    console.log(JSON.stringify(completedTasksCount, null, 2));
  } else {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
