#!/usr/bin/python3
"""
    Fetches the content of a URL and prints its type, raw content,
    and decoded content.
    """


import urllib.request


def fetch_and_print_status():
    """
    Fetches the content of a URL and prints its type, raw content,
    and decoded content.

    This function sends an HTTP GET request to a specified URL,
    retrieves the content,
    and then prints the type of the content, its raw content,
    and its decoded text in UTF-8 format.

    Args:
        None

    Returns:
        None
    """
    url = "https://alx-intranet.hbtn.io/status"

    try:
        # Send an HTTP GET request and open the response as a context manager
        with urllib.request.urlopen(url) as response:
            # Read the content of the response
            content = response.read()

            # Print the results
            print("Body response:")
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", content.decode('utf-8'))
    except urllib.error.URLError as e:
        # Handle URL-related errors, such as network issues or invalid URLs
        print("Error:", e)


if __name__ == "__main__":
    fetch_and_print_status()
