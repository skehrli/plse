#!/bin/bash

# set -x

# Check if the file path is provided as an argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <file_path>"
  exit 1
fi

file_path=$1

# Check if the file exists
if [ ! -f "$file_path" ]; then
  echo "File not found: $file_path"
  exit 1
fi

# Iterate over each line in the file
while read -r line; do
  # echo "grep -r "$line" ./repos" # | awk '{print \$1}'"
  grep -r $line ./repos #| stdbuf -oL awk '{print $1}'
done < "$file_path"

# set +x

# md relevantFiles
# while IFS= read -r line; do
#   cp "${line}" ./relevantFiles
# done < "grep.out"
# rm "grep.out"
