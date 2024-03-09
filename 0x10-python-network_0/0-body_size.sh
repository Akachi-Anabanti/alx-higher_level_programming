#!/bin/bash
# A scripts that takes a url and displays the
curl -s -o ./file.tmp -w "%{size_download}\n" "$1"
