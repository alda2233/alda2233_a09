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
from functions import file_top
# Constants

file_name = input("Enter the name of the file: ")

try:
    with open(file_name, "r", encoding="utf-8") as file_handle:
        count = int(input("Enter the number of lines to print: "))
        file_top(file_handle, count)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except ValueError:
    print("Invalid input. Please enter a valid number for the count.")
