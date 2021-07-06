import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', sep=',', index_col=0, parse_dates=True)

# Clean data
df = df[
    (df['value'] >= (df['value'].quantile(0.025))) &
    (df['value'] <= (df['value'].quantile(0.975)))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(18,5))
    plt.plot(df.index, df['value'], color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig = df_bar.plot(kind='bar', legend=True, figsize=(20,10)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=months)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    ax1 = sns.boxplot(x=df_box['year'], y=df_box['value'], ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    ax2 = sns.boxplot(x=df_box['month'], y=df_box['value'], ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
