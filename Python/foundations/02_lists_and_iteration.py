"""
Day 2 — Python Foundations
Collections: Lists & Basic Iteration

Focus:
- Creating and accessing lists
- Updating and modifying list elements
- Common list methods
- Iterating through a list
- Counting records and accumulating values
"""

# ============================================================
# 1. LISTS
# ============================================================

# A list stores multiple values in one variable.
sales = [1200, 1500, 1800, 900, 2100]

print(sales)
print(type(sales))


# Engineering notes:
# - Lists are ordered and mutable.
# - Lists allow duplicate values and mixed data types.
# - Indexing starts at 0.


# ============================================================
# 2. INDEXING & SLICING
# ============================================================

products = ["Laptop", "Phone", "Tablet", "Monitor"]

print(products[0])       # First element
print(products[1])       # Element at index 1
print(products[-1])      # Last element
print(products[-2])      # Second-last element
print(products[0:3])     # Index 0, 1, 2; end index is excluded


# Engineering notes:
# - Use indexing to access one element.
# - Use slicing to access a range.
# - Slice syntax: collection[start:end], where end is excluded.


# ============================================================
# 3. UPDATING LIST ELEMENTS
# ============================================================

sales = [1000, 1500, 2000]

sales[0] = 1200

print(sales)


# Engineering note:
# Lists are mutable: assignment at an index replaces that element.


# ============================================================
# 4. ADDING & INSERTING ELEMENTS
# ============================================================

sales = [1000, 1500, 2000]

sales.append(2500)       # Add to the end
sales.insert(1, 1250)   # Insert at index 1

print(sales)


# Engineering notes:
# - append(value) adds one item to the end.
# - insert(index, value) inserts at a position and shifts later items.


# ============================================================
# 5. REMOVING ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40]

numbers.remove(20)       # Removes the value 20
numbers.pop()            # Removes the last element

print(numbers)


# Useful patterns:
# - remove(value) removes the first matching value.
# - pop() removes and returns the last item.
# - pop(index) removes and returns the item at that index.


# ============================================================
# 6. LENGTH & SORTING
# ============================================================

sales = [450, 120, 900, 300]

sales.sort()
print(sales)
print(len(sales))


# sorted() returns a new sorted list and preserves the original.
sales = [500, 200, 800, 100]
sorted_sales = sorted(sales)

print(sorted_sales)
print(sales)


# Engineering notes:
# - len(list) returns the number of elements, not the last index.
# - list.sort() modifies the original list.
# - sorted(list) creates a new sorted list.


# ============================================================
# 7. ITERATING THROUGH A LIST
# ============================================================

sales = [1000, 1500, 2000]

for amount in sales:
    print(amount)


# Engineering note:
# A for loop processes each element in an iterable, one at a time.


# ============================================================
# 8. ACCUMULATION: CALCULATING TOTAL
# ============================================================

sales = [100, 200, 300]

total = 0

for amount in sales:
    total += amount

print("Total:", total)


# Engineering notes:
# - total += amount means total = total + amount.
# - An accumulator carries a running result across iterations.
# - Initialize the accumulator before the loop.


# ============================================================
# 9. COUNTING RECORDS
# ============================================================

sales = [100, 200, 300, 400]

count = 0

for amount in sales:
    count += 1

print("Count:", count)


# Engineering notes:
# - count += 1 increases the count by one per processed record.
# - Counting records is different from summing their values.


# ============================================================
# 10. TOTAL & COUNT TOGETHER
# ============================================================

sales = [500, 700, 900]

total = 0
count = 0

for amount in sales:
    total += amount
    count += 1

print("Total revenue:", total)
print("Number of sales:", count)


# ============================================================
# DAY 2 CHECKPOINT
# ============================================================

# Covered:
# - Creating lists
# - Indexing and slicing
# - Updating elements
# - append() and insert()
# - remove() and pop()
# - len()
# - sort() and sorted()
# - Iterating with for
# - Accumulating a total
# - Counting records
#
# Still to learn:
# - Conditional counting and filtering
# - Tuples
# - Sets
# - Dictionaries
# - Nested collections
# - Day 2 practical challenge and assessment
#
# Status: DAY 2 IN PROGRESS
