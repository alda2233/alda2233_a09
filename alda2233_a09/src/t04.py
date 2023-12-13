"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering
# Constants

input_file_name = input("Enter the name of the input file: ")
output_file_name = input("Enter the name of the output file: ")

try:
    with open(input_file_name, "r", encoding="utf-8") as fh_read, open(output_file_name, "w", encoding="utf-8") as fh_write:
        line_numbering(fh_read, fh_write)
    print("Line numbering completed successfully.")
except FileNotFoundError:
    print(f"File not found: {input_file_name}")
except Exception as e:
    print(f"An error occurred: {e}")
