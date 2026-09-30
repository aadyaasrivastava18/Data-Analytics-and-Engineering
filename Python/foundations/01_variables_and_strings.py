"""
Day 1 — Python Foundations
Variables, Data Types & Strings

Focus:
- Data types and type conversion
- String indexing and slicing
- String cleaning and normalization
- Writing readable data-processing code
"""

# ============================================================
# 1. DATA TYPES & TYPE CONVERSION
# ============================================================

price = "249.99"
quantity = "3"
discount_percent = "10"

price = float(price)
quantity = int(quantity)
discount_percent = int(discount_percent)

order_total = price * quantity
discount_amount = order_total * discount_percent / 100
final_amount = order_total - discount_amount

print(final_amount)


# Engineering note:
# Convert raw string data before performing calculations.
# Keep variable names aligned with what the value represents.


# ============================================================
# 2. STRING INDEXING & SLICING
# ============================================================

email = "aadyaa@gmail.com"

print(email[0])       # First character
print(email[-1])      # Last character
print(email[0:6])     # Characters 0–5
print(email[7:])      # From index 7 to end


# Engineering note:
# Python uses zero-based indexing.
# Slicing follows: string[start:end]
# start is included; end is excluded.


# ============================================================
# 3. STRING CLEANING
# ============================================================

city = "  nEW yORK  "

clean_city = city.strip().lower().title()

print(clean_city)


# Useful methods:
# strip()  -> removes surrounding whitespace
# lower()  -> lowercase
# upper()  -> uppercase
# title()  -> title case


# ============================================================
# 4. STRING REPLACEMENT
# ============================================================

status = "Not Active"

status = status.replace("Not Active", "Inactive")

print(status)


# ============================================================
# 5. EMAIL NORMALIZATION
# ============================================================

email = "  AADYAA@GMAIL.COM  "

clean_email = email.strip().lower()

print(clean_email)


# Engineering note:
# Normalize emails with whitespace removal + lowercase.
# Do not use title() for email addresses.


# ============================================================
# DAY 1 CHECKPOINT
# ============================================================

# Completed:
# - Variables
# - int / float / str / bool
# - Type conversion
# - Basic calculations
# - String indexing
# - Negative indexing
# - String slicing
# - strip()
# - lower() / upper() / title()
# - replace()
# - Method chaining
# - Basic data cleaning
#
# Remaining:
# - split()
# - join()
# - Day 1 mini data-cleaning challenge
# - Day 1 assessment
