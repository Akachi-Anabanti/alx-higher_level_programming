#!/bin/bash
# A scripts that takes a url and displays the body
curl -s -f -L -X GET "$1"
