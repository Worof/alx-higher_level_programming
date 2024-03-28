#!/bin/bash
# Makes a request to a specific endpoint to get a specific response from the server
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
