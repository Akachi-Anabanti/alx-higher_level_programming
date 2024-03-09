#!bin/bash
# A scripts that takes a url and displays the 
#+ size of the body of the response

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <url>"
  exit 1
fi

curl -s -o ./file.tmp -w "%{size_download}\n" "$1"
