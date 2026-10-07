"""
Day 3 — Python Foundations
Functions & Control Flow

Focus:
- Conditional logic
- Functions and reusable logic
- Parameters, arguments, return values
- Scope
- Default parameters
- Multiple return values
"""


# ============================================================
# 1. CONTROL FLOW
# ============================================================

# Definition:
# Control flow determines which code executes based on conditions.

amount = 1500

if amount >= 2000:
    category = "Large"
elif amount >= 1000:
    category = "Medium"
else:
    category = "Small"

print(category)

# Standard:
# Conditions are evaluated top-to-bottom; first True branch executes.


# ============================================================
# 2. FUNCTIONS
# ============================================================

# Definition:
# A function is a reusable block of code that performs one task.

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 3)

print(total)


# Industry standard:
# - One clear responsibility per function.
# - Use descriptive, action-oriented names.
# - Prefer reusable functions over repeated logic.


# ============================================================
# 3. PARAMETERS & ARGUMENTS
# ============================================================

def calculate_discount(price, discount_percent):
    return price - (price * discount_percent / 100)

result = calculate_discount(1000, 10)


# Parameter  → variable defined in the function
# Argument   → value passed during the function call


# ============================================================
# 4. RETURN vs PRINT
# ============================================================

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 2)
print(total)


# return → sends a value to the caller
# print  → displays a value
#
# Industry standard:
# Use return for reusable/testable logic.
# Use print mainly for output, debugging, or user-facing display.


# ============================================================
# 5. FUNCTIONS + CONDITIONS
# ============================================================

def classify_order(amount):
    if amount >= 1000:
        return "High-value"
    return "Regular"


print(classify_order(1500))


# Industry standard:
# Keep business rules inside reusable functions instead of
# duplicating conditions throughout the codebase.


# ============================================================
# 6. FUNCTIONS + COLLECTIONS
# ============================================================

def get_high_value_orders(orders):
    high_value = []

    for order in orders:
        if order >= 1000:
            high_value.append(order)

    return high_value


orders = [800, 1100, 500, 2000]

print(get_high_value_orders(orders))


# Pattern:
# Input → Process → Return


# ============================================================
# 7. DEFAULT PARAMETERS
# ============================================================

def calculate_discount(price, discount_percent=10):
    return price - (price * discount_percent / 100)


print(calculate_discount(1000))       # Default: 10%
print(calculate_discount(1000, 20))   # Override: 20%


# Definition:
# A default parameter provides a fallback value when no argument
# is supplied.


# ============================================================
# 8. VARIABLE SCOPE
# ============================================================

def calculate_total(price, quantity):
    total = price * quantity
    return total

result = calculate_total(500, 2)

print(result)


# Definition:
# Scope defines where a variable can be accessed.
#
# total  → local to the function
# result → available in the surrounding scope


# Industry standard:
# Prefer local variables and explicit inputs/outputs.
# Avoid unnecessary global state.


# ============================================================
# 9. MULTIPLE RETURN VALUES
# ============================================================

def get_stats(values):
    minimum = min(values)
    maximum = max(values)

    return minimum, maximum


numbers = [10, 5, 30, 15]

low, high = get_stats(numbers)

print(low, high)


# Definition:
# Tuple unpacking assigns multiple returned values to variables.


# ============================================================
# ENGINEERING PATTERNS
# ============================================================

# Clear naming
calculate_total()
count_high_value()
get_high_value_orders()

# Avoid vague names
# process_data()
# do_work()

# Prefer:
# Small functions
# Clear inputs
# Explicit return values
# Minimal side effects
# Reusable business logic


# ============================================================
# DAY 3 CHECKPOINT
# ============================================================

# Covered:
# Control flow | Functions | Parameters | Arguments
# return vs print | Default parameters | Scope
# Multiple return values | Tuple unpacking
#
# Still to learn:
# Practical function design
# Functions + nested data
# Day 3 practical challenge
# Day 3 assessment
#
# Status: DAY 3 IN PROGRESS
