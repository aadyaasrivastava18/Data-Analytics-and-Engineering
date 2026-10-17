
"""
Day 5 — Python Foundations
Data Processing & Cleaning

Focus: combine functions, collections, conditions, and file handling
to clean and summarize simple business data.

Core pattern: Read -> Clean -> Transform -> Analyze -> Write
"""

from pathlib import Path


# 1. Clean individual values
def clean_customer_name(name):
    """Remove surrounding whitespace and normalize capitalization."""
    return name.strip().title()


def clean_email(email):
    """Normalize email formatting for consistent comparisons."""
    return email.strip().lower()


print(clean_customer_name("  aSHA shARMA  "))  # Asha Sharma
print(clean_email("  ASHA@EXAMPLE.COM "))      # asha@example.com


# 2. Validate records
def is_valid_order(order):
    """A valid order must have a customer and a non-negative amount."""
    return (
        bool(order.get("customer", "").strip())
        and order.get("amount", -1) >= 0
    )


orders = [
    {"customer": " Asha ", "amount": 1200},
    {"customer": "Riya", "amount": 800},
    {"customer": "", "amount": 500},
    {"customer": "Neha", "amount": -100},
]

valid_orders = []

for order in orders:
    if is_valid_order(order):
        valid_orders.append(order)

print(valid_orders)


# 3. Transform records
def clean_order(order):
    """Return a cleaned copy without changing the original record."""
    return {
        "customer": clean_customer_name(order["customer"]),
        "amount": order["amount"],
    }


cleaned_orders = []

for order in valid_orders:
    cleaned_orders.append(clean_order(order))

print(cleaned_orders)


# 4. Calculate business metrics
def calculate_total_revenue(orders):
    """Return the sum of order amounts."""
    total = 0

    for order in orders:
        total += order["amount"]

    return total


def count_high_value_orders(orders, threshold=1000):
    """Count orders whose amount meets the threshold."""
    count = 0

    for order in orders:
        if order["amount"] >= threshold:
            count += 1

    return count


print(calculate_total_revenue(cleaned_orders))  # 2000
print(count_high_value_orders(cleaned_orders))  # 1


# 5. Read and process a text file
def read_clean_lines(file_path):
    """Return non-empty, whitespace-cleaned lines."""
    cleaned_lines = []

    with Path(file_path).open("r", encoding="utf-8") as file:
        for line in file:
            value = line.strip()

            if value:
                cleaned_lines.append(value)

    return cleaned_lines


# Example:
# names = read_clean_lines("data/customers.txt")
# print(names)


# 6. Write cleaned results
def write_lines(file_path, lines):
    """Write one string per line, creating parent folders if needed."""
    output_path = Path(file_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


# Example:
# write_lines("output/clean_customers.txt", names)


# 7. Handle expected file errors
def process_customer_file(input_path, output_path):
    """Read, clean, and write customer names."""
    try:
        names = read_clean_lines(input_path)
        cleaned_names = [clean_customer_name(name) for name in names]
        write_lines(output_path, cleaned_names)
        return len(cleaned_names)

    except FileNotFoundError:
        print(f"Input file not found: {input_path}")
        return 0


# Example:
# processed_count = process_customer_file(
#     "data/customers.txt",
#     "output/clean_customers.txt",
# )
# print(f"Records processed: {processed_count}")


# Engineering practices:
# - Separate cleaning, validation, analysis, and file I/O into functions.
# - Validate records before calculating business metrics.
# - Use descriptive function names and return values.
# - Avoid modifying source records when a cleaned copy is sufficient.
# - Use UTF-8 and pathlib for predictable file handling.
# - Process files line by line when practical.
# - Catch specific, expected exceptions rather than every exception.
# - Test with empty, malformed, and boundary-value records.


# Day 5 checkpoint:
# Covered: data cleaning, validation, transformation, aggregation,
# reusable file-processing functions, and error handling.
# Status: IN PROGRESS — practise and complete the Day 5 assessment.
