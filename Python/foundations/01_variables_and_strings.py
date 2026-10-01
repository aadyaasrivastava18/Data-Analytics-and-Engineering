
"""
Python Foundations
Variables, Data Types & Strings

Focus:
- Data types and type conversion
- String indexing and slicing
- String cleaning and normalization
- String splitting and joining
- Writing readable data-processing code
"""

# ============================================================
# 1. VARIABLES, DATA TYPES & TYPE CONVERSION
# ============================================================

price = "249.99"
quantity = "3"
discount_percent = "10"

# Convert raw string values into numeric types
price = float(price)
quantity = int(quantity)
discount_percent = int(discount_percent)

order_total = price * quantity
discount_amount = order_total * discount_percent / 100
final_amount = order_total - discount_amount

print("Order Total:", order_total)
print("Discount:", discount_amount)
print("Final Amount:", final_amount)


# Engineering notes:
# - Raw data may arrive as strings, even when it represents numbers.
# - Convert values before performing calculations.
# - Use meaningful variable names.
# - Keep variable names aligned with what the value represents.
# - int("249.99") raises ValueError; use float() for decimals.


# ============================================================
# 2. BASIC DATA TYPES
# ============================================================

age = 22
salary = 45000.50
name = "Aadyaa"
is_active = True

print(type(age))
print(type(salary))
print(type(name))
print(type(is_active))


# Engineering notes:
# int   -> whole numbers
# float -> decimal numbers
# str   -> text
# bool  -> True or False
#
# "100" == 100 returns False because the types differ.
# True and False are boolean values, not strings.


# ============================================================
# 3. STRING INDEXING & SLICING
# ============================================================

email = "aadyaa@gmail.com"

print(email[0])       # First character
print(email[-1])      # Last character
print(email[0:6])     # Characters at indexes 0 to 5
print(email[7:])      # From index 7 to the end
print(email[:6])      # From beginning to index 5


# Engineering notes:
# - Python uses zero-based indexing.
# - Negative indexing starts from the end.
# - Slicing follows: string[start:end]
# - Start is included; end is excluded.
# - Slicing is useful for extracting parts of strings.


# ============================================================
# 4. STRING CLEANING & NORMALIZATION
# ============================================================

city = "  nEW yORK  "

clean_city = city.strip().lower().title()

print(clean_city)


# Useful methods:
# strip()  -> removes surrounding whitespace
# lstrip() -> removes whitespace from the left
# rstrip() -> removes whitespace from the right
# lower()  -> converts to lowercase
# upper()  -> converts to uppercase
# title()  -> converts words to title case


# Engineering notes:
# - Normalize inconsistent text before analysis.
# - Method chaining allows multiple transformations.
# - Avoid title() for emails, usernames, and case-sensitive identifiers.


# ============================================================
# 5. STRING REPLACEMENT
# ============================================================

status = "Not Active"

clean_status = status.replace("Not Active", "Inactive")

print(clean_status)


# Engineering notes:
# - replace(old, new) replaces matching text.
# - Exact matching can be sensitive to capitalization and whitespace.
# - Normalize data before applying replacement when necessary.


# ============================================================
# 6. EMAIL NORMALIZATION
# ============================================================

email = "  AADYAA@GMAIL.COM  "

clean_email = email.strip().lower()

print(clean_email)


# Engineering notes:
# - Remove surrounding whitespace.
# - Convert email text to lowercase for normalization.
# - Keep raw and cleaned values separate when data lineage matters.


# ============================================================
# 7. STRING SPLITTING
# ============================================================

email = "aadyaa@gmail.com"

email_parts = email.split("@")

username = email_parts[0]
domain = email_parts[1]

print("Username:", username)
print("Domain:", domain)


# Engineering notes:
# - split() separates a string using a delimiter.
# - It returns a list.
# - Use indexing to access individual components.
# - Syntax: string.split("delimiter")
# - Validate input before assuming a component exists.


# ============================================================
# 8. STRING JOINING
# ============================================================

skills = ["Python", "SQL", "Pandas"]

result = ", ".join(skills)

print(result)


# Engineering notes:
# - join() combines strings from an iterable.
# - The separator is placed between each element.
# - Syntax: "separator".join(iterable)
# - All elements must be strings.


# ============================================================
# 9. MINI DATA-CLEANING CHALLENGE
# ============================================================

customer = "  AADYAA SRIVASTAVA  "
email = "  AADYAA@GMAIL.COM  "

# Normalize customer name
clean_customer = customer.strip().lower().title()

# Normalize email
clean_email = email.strip().lower()

# Extract email domain
email_parts = clean_email.split("@")
domain = email_parts[1]

print("Customer:", clean_customer)
print("Email:", clean_email)
print("Domain:", domain)


# Engineering notes:
# - Separate cleaning, parsing, and extraction into clear steps.
# - Intermediate variables improve readability and debugging.
# - Avoid modifying the meaning of a variable midway through processing.


# ============================================================
# DAY 1 CHECKPOINT
# ============================================================

# Completed:
# - Variables and naming
# - int / float / str / bool
# - Type conversion
# - Basic calculations
# - String indexing
# - Negative indexing
# - String slicing
# - strip() / lstrip() / rstrip()
# - lower() / upper() / title()
# - replace()
# - split() / join()
# - Method chaining
# - Email normalization
# - Basic data-cleaning challenge
#
# Engineering takeaways:
# - Convert raw data before calculations.
# - Preserve original values when useful.
# - Use meaningful variable names.
# - Normalize text before analysis.
# - Break data-processing logic into readable stages.
#
# Status: DAY 1 COMPLETE
