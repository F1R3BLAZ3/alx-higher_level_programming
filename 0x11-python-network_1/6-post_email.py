#!/usr/bin/python3
"""
    Sends a POST request to a specified URL with email data and prints
    the response body.
    """
import requests
import sys


def send_post_request(url, email):
    """
    Sends a POST request to a specified URL with email data and prints
    the response body.

    This function sends a POST request to a specified URL using the requests
    library. It includes email data in the request, and then it prints the
    body of the response.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include in the request data.

    Returns:
        None
    """
    try:
        # Define the data to be sent in the POST request
        data = {"email": email}

        # Send a POST request with the data to the specified URL
        response = requests.post(url, data=data)

        # Display the body of the response
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
