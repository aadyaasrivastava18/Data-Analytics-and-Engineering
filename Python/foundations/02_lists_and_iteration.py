"""
Day 2 — Python Foundations
Collections & Iteration

Focus:
- Lists, tuples, sets, dictionaries
- Iteration and filtering
- Nested data
"""

# ============================================================
# 1. LISTS
# ============================================================

sales = [1200, 1500, 1800, 900, 2100]

print(sales[0])       # First
print(sales[-1])      # Last
print(sales[1:4])     # Slice; end excluded

sales[0] = 1300       # Mutable
sales.append(2500)
sales.insert(1, 1250)

sales.remove(900)
sales.pop()           # Last
sales.pop(0)          # By index


# ============================================================
# 2. SORTING & LENGTH
# ============================================================

sales = [450, 120, 900, 300]

sales.sort()                  # Mutates original
sorted_sales = sorted(sales)  # Returns new list

print(len(sales))             # Number of elements


# ============================================================
# 3. ITERATION
# ============================================================

sales = [100, 200, 300]

total = 0
count = 0

for sale in sales:
    total += sale
    count += 1

print(total)
print(count)


# ============================================================
# 4. FILTERING
# ============================================================

orders = [500, 1200, 800, 1500, 2000]

high_value = []

for order in orders:
    if order >= 1000:
        high_value.append(order)

print(high_value)


# ============================================================
# 5. ENUMERATE
# ============================================================

products = ["Laptop", "Mouse", "Keyboard"]

for index, product in enumerate(products, start=1):
    print(index, product)


# ============================================================
# 6. TUPLES
# ============================================================

config = ("localhost", 5432, "analytics")

print(config[1])
print(len(config))

# Ordered + immutable


# ============================================================
# 7. SETS
# ============================================================

customer_ids = {101, 102, 101, 103}

customer_ids.add(104)
customer_ids.discard(102)

print(customer_ids)

# Unique values; no positional indexing


# ============================================================
# 8. DICTIONARIES
# ============================================================

employee = {
    "name": "Riya",
    "department": "Analytics",
    "salary": 60000
}

print(employee["department"])

employee["salary"] = 70000       # Update
employee["location"] = "India"   # Add

print(employee.get("age", 0))    # Safe access

for key, value in employee.items():
    print(key, value)


# ============================================================
# 9. NESTED DATA
# ============================================================

orders = [
    {"customer": "Asha", "amount": 500},
    {"customer": "Riya", "amount": 1200},
    {"customer": "Neha", "amount": 800}
]

for order in orders:
    if order["amount"] >= 1000:
        print(order["customer"])


# ============================================================
# ENGINEERING PATTERNS
# ============================================================

# Sum
total += value

# Count
count += 1

# Filter / collect
result.append(value)

# Nested record access
record["field"]

# Safe dictionary access
record.get("field", default)


# ============================================================
# DAY 2 CHECKPOINT
# ============================================================

# Covered:
# Lists | Iteration | Filtering | enumerate()
# Tuples | Sets | Dictionaries | Nested data
