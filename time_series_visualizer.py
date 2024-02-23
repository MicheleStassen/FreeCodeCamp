import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)

# Clean data
df = df.loc[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = df.plot.line(figsize=(15,5), color='red', legend=False);
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.groupby(pd.PeriodIndex(df_bar.index, freq="M"))['value'].mean()

    # Draw bar plot
    month_dict = {
    1:"January", 2: "February", 3: "March", 4: "April", 
    5: "May", 6: "June", 7: "July", 8: "August", 
    9: "September", 10: "October", 11: "November", 12: "December"
    }
    fig = df_bar.pivot('Year','Month','value').rename(columns=month_dict).plot.bar(figsize=(6,6))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 5))

    sns.boxplot(df_box, ax=ax1, y='value', x='year')

    mon_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(df_box, ax=ax2, y='value', x='month', order=mon_order)

    ax1.set_ylabel("Page Views")
    ax1.set_xlabel("Year")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_ylabel("Page Views")
    ax2.set_xlabel("Month")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
