#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the body
of the response (decoded in utf-8). If an error occurs, it prints
the HTTP status code.
"""
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
