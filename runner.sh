#!/bin/bash
# Bash script to run a Python script with an argument

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 {left or right}"
  exit 1
fi

# Run the Python script, passing the argument
python /home/root/pdfswiper/argreader.py "$1"