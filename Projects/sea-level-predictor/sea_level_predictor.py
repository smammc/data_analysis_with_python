import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')

    # Create scatter plot
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Create first line of best fit
    reg1 = linregress(df['Year'], y=df['CSIRO Adjusted Sea Level'])
    total_years = range(1880, 2050)
    plt.plot(total_years, (reg1.intercept + reg1.slope * total_years), color='red', label='Best Fit 1')

    # Create second line of best fit
    from_2000 = df[df['Year'] >= 2000]
    after_2000 = range(2000, 2050)
    reg2 = linregress(from_2000['Year'], from_2000['CSIRO Adjusted Sea Level'])
    plt.plot(after_2000, (reg2.intercept + reg2.slope * after_2000), color='green', label='Best Fit 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    #Handling duplicate labels
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc='upper left')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()