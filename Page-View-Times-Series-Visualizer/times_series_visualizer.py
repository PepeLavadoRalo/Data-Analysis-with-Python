import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np

# Register converters to handle datetime data properly
register_matplotlib_converters()

# Import data (make sure to parse the date column)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data by removing outliers (values outside 2.5% and 97.5% quantiles)
df = df[(df['value'] > df['value'].quantile(0.025)) & 
        (df['value'] < df['value'].quantile(0.975))]

def draw_line_plot():
    # Create a line plot of page views over time
    fig = plt.figure(figsize=(18, 6))  # Set the figure size
    plt.plot(df, color='firebrick')  # Plot the data with a red color
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')  # Title of the plot
    plt.xlabel('Date')  # Label for the x-axis
    plt.ylabel('Page Views')  # Label for the y-axis

    # Save the figure as a PNG image
    fig.savefig('line_plot.png')
    return fig  # Return the figure object

def draw_bar_plot():
    # Prepare data for the monthly bar plot
    df_bar = df.copy(deep=True)  # Create a copy of the data
    df_bar['year'] = df_bar.index.year  # Extract the year from the index (date)
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]  # Month names
    df_bar['month'] = df_bar.index.month_name()  # Extract the month name from the index
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)  # Categorize months in correct order
    
    # Create a pivot table to get the average values per year and month
    df_bar_pivot = pd.pivot_table(
        df_bar,
        values="value",
        index="year",
        columns="month",
        aggfunc=np.mean
    )

    # Create a bar plot
    fig = df_bar_pivot.plot(kind='bar').get_figure()  # Generate the bar plot
    fig.set_figheight(6)  # Set the figure height
    fig.set_figwidth(8)  # Set the figure width
    plt.xlabel('Years')  # Label for the x-axis
    plt.ylabel('Average Page Views')  # Label for the y-axis
    plt.legend(title='Months')  # Add a legend with the title 'Months'

    # Save the figure as a PNG image
    fig.savefig('bar_plot.png')
    return fig  # Return the figure object

def draw_box_plot():
    # Prepare data for the box plots
    df_box = df.copy()  # Create a copy of the data
    df_box.reset_index(inplace=True)  # Reset the index to make 'date' a column
    df_box['year'] = [d.year for d in df_box.date]  # Extract the year from the 'date' column
    df_box['month'] = [d.strftime('%b') for d in df_box.date]  # Extract the month abbreviation
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]  # Abbreviated month names
    df_box['month'] = pd.Categorical(df_box['month'], categories=months)  # Categorize months in correct order

    # Ensure the 'value' column is of type float
    df_box['value'] = df_box['value'].astype(float)

    # Create box plots for year-wise and month-wise trends
    fig, ax = plt.subplots(1, 2, figsize=(18, 6))  # Create a subplot with 1 row and 2 columns
    plt.subplot(1, 2, 1)  # First subplot (year-wise box plot)
    sns.boxplot(x=df_box['year'], y=df_box['value'])  # Create a box plot for years
    plt.title('Year-wise Box Plot (Trend)')  # Title for the first plot
    plt.xlabel('Year')  # Label for the x-axis of the first plot
    plt.ylabel('Page Views')  # Label for the y-axis of the first plot
    
    plt.subplot(1, 2, 2)  # Second subplot (month-wise box plot)
    sns.boxplot(x=df_box['month'], y=df_box['value'])  # Create a box plot for months
    plt.title('Month-wise Box Plot (Seasonality)')  # Title for the second plot
    plt.xlabel('Month')  # Label for the x-axis of the second plot
    plt.ylabel('Page Views')  # Label for the y-axis of the second plot

    # Save the figure as a PNG image
    fig.savefig('box_plot.png')
    return fig  # Return the figure object
