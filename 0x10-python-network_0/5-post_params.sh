#!/bin/bash
# A script that sends a POST request with body params
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
