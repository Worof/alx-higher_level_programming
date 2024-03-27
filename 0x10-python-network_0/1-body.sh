#!/bin/bash
#a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL --request GET "$1" -o/dev/null -w '%{http_code}' | grep -q "200" && cur; -sL "$1"