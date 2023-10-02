#!/usr/bin/python3
"""
    Sends a POST request to a specified URL with an email parameter.
    """


import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """
    Sends a POST request to a specified URL with an email parameter.

    This function sends a POST request to a given URL with an email parameter
    using urllib. It then reads and prints the content of the response.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email parameter to include in the request.

    Returns:
        None
    """
    # Create a dictionary to hold the email parameter
    data = {"email": email}

    # Encode the data for the POST request
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    try:
        # Send a POST request and open the response as a context manager
        with urllib.request.urlopen(url, data=encoded_data) as response:
            # Read the content of the response
            content = response.read()

            # Print the decoded content in UTF-8
            print(content.decode('utf-8'))
    except urllib.error.URLError as e:
        # Handle URL-related errors, such as network issues or invalid URLs
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
