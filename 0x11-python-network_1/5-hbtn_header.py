#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the value of
the variable X-Request-Id in the response header using requests package
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
