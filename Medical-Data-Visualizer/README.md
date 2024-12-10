# Medical Data Visualizer

## Description
This project contains a Python script that visualizes medical examination data. It generates two types of plots:

1. **Categorical Plot**: A count plot showing the relationship between different health indicators and whether the person has cardiovascular disease (cardio).
2. **Heatmap**: A correlation matrix heatmap visualizing the relationships between numerical features of the dataset.

## Files

### medical_data_visualizer.py
Contains functions to create:
- `draw_cat_plot()`: Generates a categorical plot.
- `draw_heat_map()`: Generates a heatmap of correlations between different features.

### main.py
Entrypoint file for development. It runs the `draw_cat_plot()` and `draw_heat_map()` functions and triggers unit tests automatically.

### test_module.py
Contains unit tests for ensuring the correctness of the visualizations:
- Tests for correct plot labels, number of bars, and heatmap values.

### medical_examination.csv
The dataset containing medical examination data including variables like age, weight, cholesterol, blood pressure, and other health indicators.

### catplot.png
Generated categorical plot showing counts of features based on the `cardio` target.

### heatmap.png
Generated heatmap visualizing correlations between numerical features.

## Installation
To run the script, ensure you have the following dependencies installed:
```bash
pip install pandas seaborn matplotlib numpy
```
## Usage
Run the script using
```bash
python main.py
```
This will generate the plots and save them as catplot.png and heatmap.png

## Testing
Unit tests are included to verify the correctness of the visualizations. Run the tests with:
```bash
python -m unittest test_module.py
```
