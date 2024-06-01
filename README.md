# README

## Overview
This repository contains a Python script for reading a CSV file and writing its contents to an Excel file. The script takes the input and output file paths as command-line arguments and can be scheduled to run at specified intervals using your operating system's task scheduler.

## Use Case
Many data visualization tools, like Tableau Public, only accept Excel spreadsheets (.xlsx) as input. This can be inconvenient if your data is stored in a comma-separated values file (.csv). This script automates the conversion process.  Instead of manually opening the CSV in Excel and exporting it as an XLSX file, you can simply run this script and it will handle the conversion for you. This saves time and effort, especially if you need to convert CSVs to XLSX files frequently.

## Prerequisites
- Python 3.7 or higher
- pandas library
- xlsxwriter library

## Installing Required Libraries
To install the required libraries, you can use the following pip commands:
```
pip install pandas
pip install XlsxWriter
```

## Usage
To run the script, you need to provide the input CSV file path and the output Excel file path as command-line arguments. Here is an example:
```
python csv_to_excel.py /path/to/input.csv /path/to/output.xlsx
```