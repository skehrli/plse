#!/bin/bash
# take a file of grep outputs
# extract the first column, remove a trailing colon
# the remaining lines are relative file locations
# copy all of them into a new directory

# set -x

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input_file> <output_dir>"
  exit 1
fi

file_path=$1
tmp_file=$(mktemp)
out_dir=$2

if [ ! -f "$file_path" ]; then
  echo "File not found: $file_path"
  exit 1
fi


awk -F':' '{print $1}' "$file_path" > "$tmp_file"

# yes | rm -r $out_dir
# mkdir $out_dir
while read -r line; do
  cp -t "$out_dir" "$line"
done < "$tmp_file"

# set +x
