#!/usr/bin/python3
"""
    Fetches the GitHub user ID using a personal access token for
    authentication.
    """
import requests
import sys


def get_github_user_id(username, personal_access_token):
    """
    Fetches the GitHub user ID using a personal access token for
    authentication.

    This function sends a GET request to the GitHub API to fetch user
    information, including the user's GitHub ID. It uses Basic Authentication
    with the provided username and personal access token.

    Args:
        username (str): Your GitHub username.
        personal_access_token (str): Your GitHub personal access token.

    Returns:
        int: The GitHub user ID.
    """
    # Create a session with Basic Authentication using the provided PAT
    session = requests.Session()
    session.auth = (username, personal_access_token)

    try:
        # Send a GET request to the GitHub API to fetch user information
        response = session.get("https://api.github.com/user")

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data["id"]
            return user_id
        else:
            print("Failed to retrieve user information. Status code:",
                  response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <GitHub_username>"
              "<Personal_Access_Token>")
        sys.exit(1)

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    user_id = get_github_user_id(username, personal_access_token)

    if user_id is not None:
        print("Your GitHub ID:", user_id)
