#!/bin/bash

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
while IFS= read -r line; do
  repo_name=$(basename "${line}" .git)
  git clone --filter=blob:none ${line} ./repos/${repo_name}
done < "$file_path"
