#!/bin/bash
# A scripts that takes a url shows OPTIONS
curl -sI "$1"  | grep "Allow" | cut -d " " -f 2-
