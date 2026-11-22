# Day 6 --- NumPy Foundations

**Repo:** `Python/02_numpy/01_numpy_foundations.md`\
**Status:** IN PROGRESS (broadcasting and retention assessment pending)

## Arrays and vectorization

``` python
import numpy as np
sales = np.array([100, 200, 300, 400])
print(sales * 2)  # [200 400 600 800]
print(sales + 50) # [150 250 350 450]
```

## Array creation

``` python
np.zeros(4)         # [0. 0. 0. 0.]
np.ones(3)          # [1. 1. 1.]
np.arange(1, 6)     # [1 2 3 4 5]
np.arange(2, 10, 2) # [2 4 6 8]
```

`np.arange(start, stop, step)` includes `start` but excludes `stop`.

## Dimensions, shape, indexing

``` python
a = np.array([100, 200, 300])
b = np.array([[100, 200, 300], [400, 500, 600]])
print(a.ndim, a.shape) # 1 (3,)
print(b.ndim, b.shape) # 2 (2, 3)
```

For 2D arrays use `[row, column]`; **both start at index 0**.

``` python
matrix = np.array([[10, 20], [30, 40], [50, 60]])
print(matrix[1, 0])     # 30
print(matrix[2, 1])     # 60
print(matrix[0:2, 0:2]) # [[10 20], [30 40]]
print(matrix[0:3, 1:2].shape) # (3, 1)
print(matrix[0:3, 1].shape)   # (3,)
```

Slice stop indexes are excluded. `1:2` preserves a 2D column; `1`
selects a 1D column.

## Vectorized comparisons and filtering

``` python
sales = np.array([100, 200, 300, 400])
print(sales > 150)         # [False True True True]
print(sales[sales > 150])  # [200 300 400]
print(sales[(sales >= 200) & (sales <= 300)]) # [200 300]
print(sales[(sales < 150) | (sales > 350)])   # [100 400]
```

-   `&` means **AND**: both conditions must hold.
-   `|` means **OR**: at least one condition must hold.
-   Parenthesize each comparison.

## Aggregation

``` python
print(np.sum(sales))  # 1000 — total
print(np.mean(sales)) # 250.0 — average
print(np.min(sales))  # 100
print(np.max(sales))  # 400
print(np.std(sales))  # ~111.80 — spread around mean
```

Standard deviation is lower when values are closer to the mean and
higher when they are more spread out.

## Practical application

``` python
daily_sales = np.array([100, 200, 300, 400])
high_sales = daily_sales[daily_sales > 150]
print("High sales:", high_sales)
print("Total:", np.sum(daily_sales))
print("Average:", np.mean(daily_sales))
```

## Engineering notes

-   Inspect `.ndim` and `.shape` before processing unfamiliar arrays.
-   Remember zero-based indexing and exclusive slice stops.
-   Distinguish totals (`sum`) from counts.
-   Use Boolean masks to filter numerical data.

## Checkpoint

**Covered:** creation, `arange`, shape, indexing, slicing, element-wise
operations, comparisons, Boolean filtering, AND/OR, sum, mean, min, max,
and the meaning of standard deviation.

**Remaining:** broadcasting, applied practice, Day 6 retention
assessment. **Do not mark Day 6 complete yet.**
