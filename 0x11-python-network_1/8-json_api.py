#!/usr/bin/python3
"""
    Sends a POST request to a search_user endpoint with a letter parameter
    and prints the response.
    """
import requests
import sys


def search_user_by_letter(letter):
    """
    Sends a POST request to a search_user endpoint with a letter parameter
    and prints the response.

    This function sends a POST request to a specified URL with a letter
    parameter using the requests library. It expects a JSON response with user
    information and prints the user's ID and name. If no user is found,
    it prints "No result". If the response is not valid JSON,
    it prints "Not a valid JSON".

    Args:
        letter (str): The letter to search for in the user database.

    Returns:
        None
    """
    # Define the URL to send the POST request to
    url = "http://0.0.0.0:5000/search_user"

    try:
        # Send a POST request with the letter as a parameter
        response = requests.post(url, data={"q": letter})

        # Try to parse the response as JSON
        try:
            data = response.json()

            # Check if the JSON response is properly formatted and not empty
            if isinstance(data, dict) and data:
                print("[{}] {}".format(data.get("id"), data.get("name")))
            else:
                print("No result")

        except ValueError:
            # Handle JSON parsing error
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    # Check if an argument (letter) is provided, and set q accordingly
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user_by_letter(letter)
