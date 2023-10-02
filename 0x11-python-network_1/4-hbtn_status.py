#!/usr/bin/python3
"""
    Fetches and prints the content of a given URL using the requests library.
    """
import requests


def fetch_url_content(url):
    """
    Fetches and prints the content of a given URL using the requests library.

    This function sends an HTTP GET request to a specified URL using the
    requests library, and then prints the content of the response.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        None
    """
    try:
        response = requests.get(url)
        # Raise an exception if the requestwas not successful
        response.raise_for_status()

        content = response.text

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    fetch_url_content(url)
