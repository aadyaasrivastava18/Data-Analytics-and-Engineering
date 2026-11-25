# Day 6 --- NumPy Broadcasting

**Repository:** `Python/02_numpy/02_numpy_broadcasting.md`

## 1. Broadcasting

Broadcasting enables element-wise operations between arrays with
compatible shapes without explicitly repeating input data.

``` python
import numpy as np
sales = np.array([100, 200, 300])
print(sales * 2 + 50)  # [250 450 650]
```

## 2. Shape compatibility

Compare dimensions from right to left. Each pair must be equal or
contain a dimension of size 1. Missing leading dimensions are treated as
1.

  Shape A   Shape B   Compatible   Result shape
  --------- --------- ------------ --------------
  (4, 3)    (3,)      Yes          (4, 3)
  (5, 4)    (1, 4)    Yes          (5, 4)
  (4, 3)    (4, 1)    Yes          (4, 3)
  (3, 4)    (2,)      No           ValueError
  (3, 4)    (1, 5)    No           ValueError

**Every dimension pair must be compatible.** One compatible pair cannot
compensate for an incompatible pair.

## 3. Applying values across rows and columns

``` python
sales = np.array([[100, 200, 300],
                  [400, 500, 600]])

# Same bonus vector applied to each row
bonus = np.array([10, 20, 30])
print(sales + bonus)
# [[110 220 330]
#  [410 520 630]]

# Different bonus for each row
bonus = np.array([[10], [20]])
print(sales + bonus)
# [[110 210 310]
#  [420 520 620]]
```

## 4. Debugging incompatible shapes

``` python
sales = np.array([[100, 200],
                  [300, 400],
                  [500, 600]])
bonus = np.array([10, 20, 30])  # (3,)
# sales + bonus raises ValueError: (3, 2) vs (3,)
# Rightmost dimensions 2 and 3 are incompatible.

bonus = np.array([[10], [20], [30]])  # (3, 1)
print(sales + bonus)
# [[110 210]
#  [320 420]
#  [530 630]]
```

A 1D array with three elements has shape `(3,)`; a 2D column array has
shape `(3, 1)`. Inspect `.shape` before performing operations.

## 5. Practical analytics

``` python
sales = np.array([[100, 200, 300],
                  [400, 500, 600]])
growth = np.array([1.10, 1.20, 1.30])
print(sales * growth)
# [[110. 240. 390.]
#  [440. 600. 780.]]

orders = np.array([200, 500, 800, 300, 1200])
high_orders = orders[orders >= 500]
print(np.sum(high_orders))  # 2500
```

## 6. Assessment revision

``` python
arr = np.arange(4, 20, 4)
print(arr)        # [4 8 12 16]
print(arr.shape)  # (4,)

sales = np.array([100, 200, 300, 400, 500, 600])
print(sales[(sales < 200) | (sales >= 500)])
# [100 500 600]
```

-   `arange`: start inclusive, stop exclusive, step determines
    increment.
-   `<` excludes equality; `>=` includes equality.
-   `&` requires both conditions; `|` requires at least one.
-   Debugging requires identifying the cause and rewriting the code, not
    just predicting the intended output.

## Day 6 checkpoint

-   Initial assessment: 7.5/10 (75%).
-   Passing threshold: 80%.
-   Targeted retest: first two questions correct; third question
    pending.
-   Strong areas: indexing, slicing, vectorized arithmetic, aggregation
    and practical filtering.
-   Remaining: independently explain and fix incompatible broadcasting
    shapes.
-   Status: **IN PROGRESS** --- final debugging retest not yet passed.
