# Mean-Variance-Standard Deviation Calculator

This project is a Python script that calculates statistical measures (mean, variance, standard deviation, max, min, and sum) for a 3x3 matrix created from a list of 9 numbers. The calculations are performed along rows, columns, and for the flattened matrix.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Installation](#installation)
- [Example Output](#example-output)


---

## Description

The `calculate()` function in this project performs the following:

- Accepts a list of exactly 9 numbers as input.
- Converts the list into a 3x3 NumPy matrix.
- Calculates statistical measures:
  - Mean
  - Variance
  - Standard Deviation
  - Maximum
  - Minimum
  - Sum
- Returns these calculations in a dictionary with results for rows, columns, and the flattened matrix.

If the input list contains fewer than 9 numbers, the function raises a `ValueError`.

---

## Usage

### Input
A list of 9 numbers.

### Output
A dictionary containing statistical calculations in the following format:
```python
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

## Example Output
```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

```
