import pandas as pd
import os
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Read a CSV file and write it to an Excel file.')
parser.add_argument('input_file', help='Path to the input CSV file')
parser.add_argument('output_file', help='Path to the output Excel file')

# Parse arguments
args = parser.parse_args()
input_path = args.input_file
output_path = args.output_file

# Read the CSV file with error handling
try:
    df = pd.read_csv(input_path)
    print(f"Successfully read {input_path}")
except FileNotFoundError:
    print(f"Error: The file {input_path} was not found.")
    raise
except pd.errors.EmptyDataError:
    print("Error: No data found in the file.")
    raise
except pd.errors.ParserError:
    print("Error: Parsing error while reading the file.")
    raise
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    raise

# Write to Excel with error handling
try:
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    print(f"Successfully wrote to {output_path}")
except Exception as e:
    print(f"An error occurred while writing to Excel: {e}")
    raise
