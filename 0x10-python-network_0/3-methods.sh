#!/bin/bash
# A scripts that takes a url shows OPTIONS
curl -s -X OPTIONS -I "$1"
