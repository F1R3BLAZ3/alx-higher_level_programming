#!/usr/bin/python3
"""
    Fetches the 'X-Request-Id' header from an HTTP GET request to a specified
    URL.
   """


import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches the 'X-Request-Id' header from an HTTP GET request to a specified
    URL.

    This function sends an HTTP GET request to a given URL and checks if
    the response contains the 'X-Request-Id' header. If found,
    it prints the value of the header; otherwise,
    it prints a message indicating that the header was not found.

    Args:
        url (str): The URL to send the HTTP GET request to.

    Returns:
        None
    """
    try:
        # Send an HTTP GET request and open the response as a context manager
        with urllib.request.urlopen(url) as response:
            # Check if the "X-Request-Id" header is present in the response
            if "X-Request-Id" in response.headers:
                x_request_id = response.headers["X-Request-Id"]
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response")
    except urllib.error.URLError as e:
        # Handle URL-related errors, such as network issues or invalid URLs
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
