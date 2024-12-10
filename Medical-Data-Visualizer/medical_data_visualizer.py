import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column: Calculate if the person is overweight based on BMI (weight/height^2)
# The BMI threshold is 25. If the BMI is greater than 25, the person is considered overweight.
df['overweight'] = (df['weight']/((df['height']/100)**2) > 25).astype(int)

# Normalize data for 'cholesterol' and 'gluc' columns
# If the value is 1, mark it as 0 (good), otherwise, mark it as 1 (bad)
df[['gluc','cholesterol']] = (df[['gluc','cholesterol']] > 1).astype(int)

# Function to draw a categorical plot showing counts of each variable split by the 'cardio' target.
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt`
    # The DataFrame will be reshaped to contain the 'cardio' column as identifier 
    # and the selected health indicators as value variables
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. 
    # This step is necessary to create a plot that counts the occurrences of each combination of 'cardio' and other health indicators.
    # df_cat = None (This line needs to be updated if grouping is needed explicitly)

    # Draw the categorical plot (countplot) with 'sns.catplot()'
    # The 'hue' parameter differentiates the data based on the values in the 'value' column
    fig = sns.catplot(data = df_cat, kind='count',  x='variable', hue='value', col='cardio').set(ylabel = 'total').fig

    # Save the generated plot as a .png file
    fig.savefig('catplot.png')
    return fig


# Function to draw a heat map for visualizing correlations between numerical features
def draw_heat_map():
    # Clean the data: filter out outliers based on blood pressure, height, and weight
    df_heat = df[ 
        ( df['ap_lo'] <= df['ap_hi'] ) & # Ensure diastolic pressure is less than systolic pressure
        ( df['height'] >= df['height'].quantile(0.025) ) & # Exclude extreme heights (below the 2.5 percentile)
        ( df['height'] <= df['height'].quantile(0.975) ) & # Exclude extreme heights (above the 97.5 percentile)
        ( df['weight'] >= df['weight'].quantile(0.025) ) & # Exclude extreme weights (below the 2.5 percentile)
        ( df['weight'] <= df['weight'].quantile(0.975) ) # Exclude extreme weights (above the 97.5 percentile)
    ]

    # Calculate the correlation matrix for the cleaned data
    corr = df_heat.corr()

    # Generate a mask to hide the upper triangle of the heatmap (for better readability)
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax =  plt.subplots()
    
    # Draw the heatmap using Seaborn's heatmap function
    # 'annot=True' to show correlation values, 'mask' to hide the upper triangle
    # 'fmt' specifies the format of the annotations (show only one decimal)
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt='0.1f', square=True)

    # Save the generated heatmap as a .png file
    fig.savefig('heatmap.png')
    return fig
