$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $('#add_item').click(function () {
    // Create a new <li> element
    const newItem = $('<li>Item</li>');

    // Append the new <li> element to the list (UL.my_list)
    $('ul.my_list').append(newItem);
  });
});
