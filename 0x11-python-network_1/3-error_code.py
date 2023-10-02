#!/usr/bin/python3
"""
    Fetches and prints the content of a given URL.
    """


import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    """
    Fetches and prints the content of a given URL.

    This function sends an HTTP GET request to a specified URL using urllib,
    opens the response as a context manager, and reads and prints the content
    of the response.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        None
    """
    try:
        # Send an HTTP GET request and open the response as a context manager
        with urllib.request.urlopen(url) as response:
            # Read the content of the response
            content = response.read()

            # Print the decoded content in UTF-8
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the status code
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    fetch_url_content(url)
