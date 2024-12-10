# Demographic Data Analyzer

This project analyzes demographic data extracted from the 1994 U.S. Census Database. It calculates various metrics such as the average age of men, percentage of people with a Bachelor's degree, and the most popular occupation for high earners in India.

## Features

- Count of each race in the dataset.
- Average age of men.
- Percentage of people with a Bachelor's degree.
- Analysis of higher and lower education levels with respect to income.
- Minimum working hours and the percentage of high earners in that group.
- Country with the highest percentage of high earners.
- Most popular occupation among high earners in India.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PepeLavadoRalo/demographic-data-analyzer.git
  ```
2. Navigate to the project directory
  ```bash
  cd demographic-data-analyzer
  ```
3.Install dependencies (Pandas is required):
```bash
pip install pandas
```
## Usage
1. Place the dataset adult_data.csv in the project directory.
2. Run the script to calculate and display results:
   ```bash
   python demographic_data_analyzer.py
  ```
3.To run the tests
  ```bash
  python main.py
  ```

## Tests
Unit tests are provided in test_module.py to ensure the correctness of all calculations.

## Dataset Source
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.
