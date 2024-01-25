#!/bin/bash

# Check if the file path is provided as an argument
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <file_path> <output_file>"
  exit 1
fi

file_path=$1
out_file=$2

# Check if the file exists
if [ ! -f "$file_path" ]; then
  echo "File not found: $file_path"
  exit 1
fi

if [ ! -f "$file_path" ]; then
  echo "File not found: $out_file"
  exit 1
fi

# Iterate over each line in the file
while IFS= read -r line; do
  # Call another script with the current line as an argument
  temp_file=$(mktemp)
  echo "$line" > "$temp_file"
  cat "$temp_file"
  ./query-github.sh "$temp_file" 1 >> "$out_file"
  # rm "$temp_file"
done < "$file_path"
