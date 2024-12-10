import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import unittest

def draw_plot():
    # Read data from the CSV file, converting to float and renaming columns for easier access
    df = pd.read_csv("./epa-sea-level.csv", float_precision="legacy").rename(
        columns={
            "Year": "year",  # Rename 'Year' column to 'year'
            "CSIRO Adjusted Sea Level": "sea",  # Rename 'CSIRO Adjusted Sea Level' column to 'sea'
        }
    )

    # Create a scatter plot of the data (year vs. sea level)
    plt.figure(1, figsize=(16, 9))  # Set the figure size to 16x9 inches
    plt.scatter(df["year"], df["sea"])  # Plot data as points

    # Create the first line of best fit using all the data
    regress = linregress(df["year"], df["sea"])  # Perform linear regression to get slope and intercept

    # Add future predictions up to the year 2050
    last_year = df["year"].max()  # Get the most recent year in the data
    df = df.append([{"year": y} for y in range(last_year + 1, 2050)])  # Add rows for future years

    # Plot the line of best fit (red line) for the entire dataset (past and future)
    plt.plot(
        df["year"], 
        regress.intercept + regress.slope * df["year"],  # Use linear equation to predict sea levels
        c="r",  # Red color for the line
        label="fit all"  # Label for the legend
    )

    # Create the second line of best fit using only the data from the year 2000 onwards
    df_recent = df.loc[(df["year"] >= 2000) & (df["year"] <= last_year)]  # Filter data from 2000 to the latest year
    bestfit = linregress(df_recent["year"], df_recent["sea"])  # Perform linear regression on the recent data
    df_recent = df_recent.append([{"year": y} for y in range(last_year + 1, 2050)])  # Add future years to recent data

    # Plot the second line of best fit (blue line) for the recent data (2000 to present)
    plt.plot(
        df_recent["year"],
        bestfit.intercept + bestfit.slope * df_recent["year"],  # Use linear equation to predict future sea levels
        c="b",  # Blue color for the line
        label="fit recent"  # Label for the legend
    )

    # Add axis labels and a title to the plot
    plt.xlabel("Year")  # X-axis label
    plt.ylabel("Sea Level (inches)")  # Y-axis label
    plt.title("Rise in Sea Level")  # Title of the plot

    return plt.gca()  # Return the current axis object for further customization if needed
