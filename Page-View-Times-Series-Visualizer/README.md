# Time Series Data Visualization

This project visualizes time series data from the freeCodeCamp forum page views, spanning from May 2016 to December 2019. The dataset is used to create three types of data visualizations to help understand the trends and patterns in the data. The visualizations include:

- **Line Plot**: Displays the daily page views over time.
- **Bar Plot**: Shows the average daily page views for each month, grouped by year.
- **Box Plot**: Provides a box plot showing the distribution of page views across different years and months.

## Project Structure

The project includes the following files:

- **time_series_visualizer.py**: Contains the functions that generate the three visualizations.
- **test_module.py**: Includes unit tests for the project to ensure data cleaning and visualizations work as expected.
- **main.py**: A script for testing the visualizations.
- **fcc-forum-pageviews.csv**: The dataset containing daily forum page views data.
- **line_plot.png**: Generated line plot visualization.
- **bar_plot.png**: Generated bar plot visualization.
- **box_plot.png**: Generated box plot visualization.

## Requirements

The project requires the following Python libraries:

- `matplotlib`
- `pandas`
- `seaborn`
- `numpy`
- `unittest`

You can install the required libraries using `pip`:

```bash
pip install matplotlib pandas seaborn numpy
```

