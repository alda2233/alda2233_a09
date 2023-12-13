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
from functions import file_statistics
# Constants

file_name = input("Enter the name of the file: ")

try:
    with open(file_name, "r", encoding="utf-8") as file_handle:
        ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
        print("File Statistics:")
        print(f"Uppercase Letters: {ucount}")
        print(f"Lowercase Letters: {lcount}")
        print(f"Digits: {dcount}")
        print(f"Whitespace Characters: {wcount}")
        print(f"Remaining Characters: {rcount}")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
