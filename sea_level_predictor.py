import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(7, 6))
    ax = plt.axes()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linregress_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.axline((0, linregress_1.intercept), slope=linregress_1.slope)

    # Create second line of best fit
    linregress_2 = linregress(df.loc[df['Year'] >= 2000]['Year'], df.loc[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    ax.axline((0, linregress_2.intercept), slope=linregress_2.slope)

    ax.set_xlim(1870, 2050)
    ax.set_ylim(-1, 16)

    # Add labels and title
    ax.set_ylabel("Sea Level (inches)")
    ax.set_xlabel("Year")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
