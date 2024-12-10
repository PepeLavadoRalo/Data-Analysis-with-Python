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

## Usage

### Data Cleaning and Visualization

The code in `time_series_visualizer.py` reads the CSV file and cleans the data by filtering out the top and bottom 2.5% of page views. The cleaned data is then used to generate three visualizations:

- **Line Plot**: Displays the daily page views from May 2016 to December 2019.
- **Bar Plot**: Shows the average daily page views for each month, grouped by year.
- **Box Plot**: Visualizes the distribution of page views for each year and month.

To generate the plots, simply run the functions defined in `time_series_visualizer.py`:

```python
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Generate the line plot
draw_line_plot()

# Generate the bar plot
draw_bar_plot()

# Generate the box plot
draw_box_plot()
```
The plots will be saved as `line_plot.png`, `bar_plot.png`, and `box_plot.png` in the same directory.

### Testing

Unit tests are included in the `test_module.py` file to ensure that the data cleaning process and visualizations work as expected. The tests check for:

- Correct data cleaning (after removing outliers).
- Correct titles, labels, and data in the line plot, bar plot, and box plot.

To run the tests, use the following command:
```bash
python -m unittest test_module.py
```
### Example Output

- **Bar Plot**: A bar chart showing the average page views per month across years.
- **Box Plot**: Two adjacent box plots showing the distribution of page views by year and by month.

### Conclusion

This project demonstrates how to visualize time series data using Python with pandas, matplotlib, and seaborn. It helps identify trends, seasonality, and outliers in the data.



