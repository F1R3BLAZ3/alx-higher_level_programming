#!/usr/bin/python3
"""
    Fetches and prints the 'X-Request-Id' header from the response
    of a given URL.
    """
import requests
import sys


def fetch_x_request_id(url):
    """
    Fetches and prints the 'X-Request-Id' header from the response
    of a given URL.

    This function sends an HTTP GET request to a specified URL using the
    requests library, and then checks if the 'X-Request-Id' header is present
    in the response. If found, it prints the value of the header; otherwise,
    it prints a message indicating that the header was not found.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        None
    """
    try:
        response = requests.get(url)

        # Check if the "X-Request-Id" header is present in the response
        if "X-Request-Id" in response.headers:
            x_request_id = response.headers["X-Request-Id"]
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    fetch_x_request_id(url)
