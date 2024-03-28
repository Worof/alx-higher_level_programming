#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the body
of the response. If the HTTP status code is >= 400, prints the
status code.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
