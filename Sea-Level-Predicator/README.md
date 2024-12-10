# Sea Level Prediction and Plotting

This project is designed to analyze the rise in sea levels over time based on historical data and predict future trends. The program uses a CSV file containing historical sea level data, performs linear regression to generate a line of best fit, and plots the results.

## Project Structure

The project consists of the following files:

- **`main.py`**: Main entry point of the program. It loads the data, generates the plot, and saves it as an image (`sea_level_plot.png`).
- **`draw_plot.py`**: Contains the `draw_plot()` function, which handles data processing, plotting, and the generation of two lines of best fit (for the full dataset and recent data).
- **`test_module.py`**: A test suite for validating the functions in the project. It ensures that the code runs correctly.
- **`epa-sea-level.csv`**: The CSV file containing historical sea level data, which is used to create the plot and make predictions.
- **`sea_level_plot.png`**: The output image of the generated plot, showing the rise in sea level with predictions.

## Requirements

To run this project, you need to have Python 3 and the following libraries installed:

- pandas
- matplotlib
- scipy

You can install the required libraries using `pip`:

```bash
pip install pandas matplotlib scipy
```
## Usage

### Running the program

To generate the sea level plot, simply run the main.py script:

```bash
python main.py
```
This will read the data from epa-sea-level.csv, generate the plot, and save it as sea_level_plot.png in the current directory.

### Testing
You can run the tests in test_module.py to ensure the functions work correctly. To run the tests, use the following command:
```bash
python -m unittest test_module.py
```
This will execute the test cases and display the results in the terminal.

## How it Works

- **Data Loading and Preprocessing**: The `draw_plot.py` script loads the sea level data from the CSV file (`epa-sea-level.csv`). The data is processed by renaming the columns for easier access, and the year and sea level data are extracted.

- **Scatter Plot**: A scatter plot of the data points (year vs. sea level) is created.

- **Linear Regression**: Two lines of best fit are generated:
  - The first line is based on all available data.
  - The second line is based on recent data (from the year 2000 to the latest year in the dataset).
  - Both lines of best fit are extended to predict future sea levels up to the year 2050.

- **Plotting**: The scatter plot and the lines of best fit are plotted using Matplotlib. The plot is saved as an image (`sea_level_plot.png`).

## Example Output

The output is a plot saved as `sea_level_plot.png`. The plot will show the rise in sea level from the available data and two predicted lines of best fit, one for the entire dataset and one for recent data.




