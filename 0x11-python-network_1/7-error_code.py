#!/usr/bin/python3
"""
    Sends a GET request to a specified URL and prints the response body.
    """
import requests
import sys


def send_get_request(url):
    """
    Sends a GET request to a specified URL and prints the response body.

    This function sends a GET request to a specified URL using the requests
    library. It prints the body of the response and checks the HTTP status
    code. If the status code is greater than or equal to 400, it prints an
    error message.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        None
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Display the body of the response
        print(response.text)

        # Check if the HTTP status code is greater than or equal to 400
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    send_get_request(url)
