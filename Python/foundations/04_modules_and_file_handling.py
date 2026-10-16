```python
"""
Day 4 — Python Foundations
Modules & File Handling

Focus: imports, paths, reading/writing text files, and handling missing files.
"""

# 1. Importing modules
import math

print(math.sqrt(25))   # 5.0
print(math.ceil(4.2))  # 5
print(math.floor(7.9)) # 7

# Import a specific function when useful.
from math import ceil
print(ceil(4.2))       # 5


# 2. Create and reuse your own modules
# Keep related reusable functions in a separate .py file.
# Example: calculations.py
#
# def multiply(a, b):
#     return a * b
#
# In main.py (same directory):
# from calculations import multiply
# print(multiply(4, 5))  # 20


# 3. File paths with pathlib
from pathlib import Path

file_path = Path("data/customers.json")

print(file_path.name)    # customers.json
print(file_path.stem)    # customers
print(file_path.suffix)  # .json
print(file_path.parent)  # data

# Path attribute reference:
# .name   -> filename with extension
# .stem   -> filename without extension
# .suffix -> file extension
# .parent -> containing directory

# Path checks
print(file_path.exists())  # True if the path exists
print(file_path.is_file()) # True if it is a file
print(file_path.is_dir())  # True if it is a directory


# 4. Read a text file
input_path = Path("data/notes.txt")

if input_path.is_file():
    with input_path.open("r", encoding="utf-8") as file:
        content = file.read()  # str: entire file content
    print(content)

# Reading methods:
# read()      -> str: entire file as one string
# readlines() -> list[str]: one string per line
# Iterating over the file processes one line at a time.


# 5. Read line by line
# Prefer iteration for large files to avoid loading all content at once.
if input_path.is_file():
    with input_path.open("r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())  # Removes surrounding whitespace/newlines


# 6. Write and append
output_path = Path("output/result.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)

# "w" creates or overwrites the file.
with output_path.open("w", encoding="utf-8") as file:
    file.write("Processing complete\n")

# "a" preserves existing content and appends.
with output_path.open("a", encoding="utf-8") as file:
    file.write("Another record\n")

# File modes:
# "r" -> read an existing file
# "w" -> create or overwrite; previous content is lost
# "a" -> append while preserving existing content

# Write multiple records by opening the file once.
customers = ["Asha", "Riya", "Neha"]

with output_path.open("w", encoding="utf-8") as file:
    for customer in customers:
        file.write(customer + "\n")

# Engineering note: avoid opening with "w" inside the loop,
# because each opening overwrites the previous content.


# 7. Handle a missing input file
try:
    with Path("data/sales.txt").open("r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("Input file not found")

# Read mode does not create a missing file.
# Catch expected errors with specific exception types.


# 8. Simple text-cleaning pipeline: read -> transform -> write
source_path = Path("data/customers.txt")
clean_path = Path("output/clean_customers.txt")
clean_path.parent.mkdir(parents=True, exist_ok=True)

if source_path.is_file():
    with source_path.open("r", encoding="utf-8") as source:
        with clean_path.open("w", encoding="utf-8") as destination:
            for line in source:
                clean_name = line.strip()
                destination.write(clean_name + "\n")

# ETL connection:
# Extract -> read input
# Transform -> clean whitespace
# Load -> write cleaned output


# 9. Common file-handling mistakes
# - len(lines) counts list items; it does not sum numeric values.
# - read() returns str; readlines() returns list[str].
# - strip() removes whitespace from both ends, not inside the text.
# - "w" overwrites; "a" appends.
# - mkdir() creates directories, not the output file itself.
# - Opening a missing file in "r" mode raises FileNotFoundError.


# Engineering practices:
# - Use pathlib for readable, cross-platform path handling.
# - Use with to close files reliably.
# - Specify text encoding explicitly.
# - Use "w" carefully because it overwrites existing content.
# - Use "a" to preserve content and append records.
# - Handle expected errors with specific exceptions.
# - Iterate over large text files line by line.
# - Validate inputs before processing.


# Day 4 checkpoint:
# Covered: imports, reusable modules, pathlib, file checks,
# reading methods, line iteration, writing, appending, error handling,
# and a basic text-cleaning pipeline.
# Status: IN PROGRESS — pass the Day 4 assessment before marking done.
```
