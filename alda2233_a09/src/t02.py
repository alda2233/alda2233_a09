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
from functions import read_integers
# Constants

file_name = input("Enter the name of the file: ")

try:
    with open(file_name, "r", encoding="utf-8") as file_handle:
        numbers = read_integers(file_handle)
        print("Numbers extracted from the file:", numbers)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
