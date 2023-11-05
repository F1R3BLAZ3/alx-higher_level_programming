$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $("#toggle_header").click(function () {
    // Toggle the "red" and "green" classes of <header>
    $("header").toggleClass("red green");
  });
});
