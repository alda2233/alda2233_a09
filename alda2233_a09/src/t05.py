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
from functions import student_stats
# Constants

file_name = input("Enter the name of the student information file: ")

try:
    with open(file_name, "r", encoding="utf-8") as file_handle:
        l_id, h_id, avg = student_stats(file_handle)
        print("Student Statistics:")
        print(f"Student with the Lowest Mark (ID): {l_id}")
        print(f"Student with the Highest Mark (ID): {h_id}")
        print(f"Average Mark: {avg:.2f}")
except FileNotFoundError:
    print(f"File not found: {file_name}")
except Exception as e:
    print(f"An error occurred: {e}")
