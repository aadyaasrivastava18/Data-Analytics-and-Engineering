# Day 5 — Data Processing & Cleaning

## Why this exists

Real-world data often contains inconsistent text, incomplete records, invalid values, and blank lines. A reliable data workflow cleans and validates data before transforming or analyzing it.

**Core workflow:** Read → Clean → Validate → Transform → Analyze → Write

## 1. Clean individual values

```python
def clean_customer_name(name):
    return name.strip().title()


def clean_email(email):
    return email.strip().lower()
```

- `strip()` removes leading and trailing whitespace.
- `title()` normalizes name capitalization.
- `lower()` makes email comparisons consistent.

## 2. Validate records

```python
def is_valid_order(order):
    return (
        bool(order.get("customer", "").strip())
        and order.get("amount", -1) >= 0
    )
```

A record is valid only when both conditions are true:
- Customer name is not empty after whitespace is removed.
- Amount is non-negative.

An empty string evaluates to `False`:

```python
bool("   ".strip())  # False
bool("Neha".strip()) # True
```

Use validation before calculating business metrics.

## 3. Transform records without changing the source

```python
def clean_order(order):
    return {
        "customer": order["customer"].strip().title(),
        "amount": order["amount"],
    }


order = {"customer": "  rIYA  ", "amount": 800}
cleaned = clean_order(order)

print(cleaned)  # {"customer": "Riya", "amount": 800}
print(order)    # Original record remains unchanged
```

Returning a new dictionary avoids modifying the original record.

## 4. Calculate business metrics

### Running total

```python
total = 0

for amount in [500, 1200, 800, 1500]:
    total += amount

print(total)  # 4000
```

### Conditional count

```python
count = 0

for amount in [500, 1200, 800, 1500]:
    if amount >= 1000:
        count += 1

print(count)  # 2
```

### Total and count together

```python
total = 0
count = 0

for amount in [500, 1200, 800, 1500]:
    total += amount
    if amount >= 1000:
        count += 1

# total = 4000
# count = 2
```

**Remember:**
- `total += amount` adds the value to a running sum.
- `count += 1` counts records that meet a condition.
- Initialize accumulators before the loop.

## 5. Read and clean a text file

```python
def read_clean_lines(file_path):
    cleaned_lines = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            value = line.strip()
            if value:
                cleaned_lines.append(value)

    return cleaned_lines
```

Key behavior:
- Iterating over the file reads it one line at a time.
- `strip()` removes surrounding whitespace and newline characters.
- `if value` skips blank or whitespace-only lines.
- The function returns a list of cleaned strings.

For example, lines containing `Asha`, a blank line, and `Riya` produce:

```python
["Asha", "Riya"]
```

## 6. Write processed results

```python
from pathlib import Path


def write_lines(file_path, lines):
    output_path = Path(file_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")
```

- `"w"` creates a file or overwrites its existing content.
- `"a"` appends to existing content.
- `mkdir(parents=True, exist_ok=True)` creates missing parent folders.
- `with` closes the file automatically.

## 7. Handle expected file errors

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

Catch specific, expected exceptions. A missing input file raises `FileNotFoundError`; the matching `except` block handles it.

## Engineering practices

- Separate cleaning, validation, transformation, analysis, and file I/O.
- Validate records before aggregating them.
- Use descriptive function names and return values.
- Avoid changing source records when a cleaned copy is sufficient.
- Use UTF-8 for text files.
- Process large files line by line when practical.
- Test empty, malformed, and boundary-value records.
- Catch specific exceptions rather than using a broad `except` without a reason.

## Interview explanation

“I build small, reusable functions for cleaning and validating records before analysis. I use loops and accumulators for business metrics, and process files with context managers so resources are closed reliably. I also handle expected errors, such as missing input files.”

## Common mistakes

- Treating a whitespace-only string as valid without calling `strip()`.
- Confusing a running total with a conditional count.
- Placing `total += amount` inside a condition when the requirement is to sum every record.
- Forgetting that `read_clean_lines()` returns a list.
- Assuming `strip()` removes blank lines from a file by itself; the `if value` check skips them.
- Using `"w"` when the intention is to append.

## Key takeaways

- Clean values before comparing or analyzing them.
- Validate records before using them.
- Keep source data unchanged when possible.
- Distinguish totals from conditional counts.
- Use `strip()` plus a truthiness check to skip blank lines.
- Use context managers and specific exception handling for file operations.

## Day 5 checkpoint

**Status: COMPLETE — passed the targeted retention retest (2/2) after reviewing weak areas.**

Topics covered: data cleaning, record validation, non-mutating transformations, business metrics, text-file processing, writing results, and file error handling.
