#!/bin/bash

# Input file path
input_file="files/samplegut.txt"

# Python script path
python_script="scripts/biosample_extraction.py"

# Read each line from the input file
while IFS=$'\t' read -r -a columns; do
    # Extract the first and second columns
    column1=${columns[0]}
    column2=${columns[1]}
    
    # Remove leading/trailing whitespace from the columns
    column1=$(echo "$column1" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
    column2=$(echo "$column2" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
    
    # Set the output file name as the first column
    output_file="$column1.txt"
    
    # Run the Python script with the second column as an argument
    python3 "$python_script" -s "$column2" --out files/biosamples_data/biosamples_ids_gut/"$output_file" -e alex.kushnareva99@gmail.com
    
    echo "Output file $output_file created."
done < "$input_file"
