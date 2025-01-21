import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

"""

For this project you will visualize time series data using a line chart, bar chart, and box plots. 
You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page 
views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations 
will help you understand the patterns in visits and identify yearly and monthly growth.

Use the data to complete the following tasks:

-Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
-Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or 
bottom 2.5% of the dataset.
Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". 
The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date 
and the label on the y axis should be Page Views.
Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show 
average daily page views for each month grouped by year. The legend should show month labels and have a title 
of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be 
Average Page Views.
Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to 
"examples/Figure_3.png". These box plots should show how the values are distributed within a 
given year or month and how it compares over time. The title of the first chart should be 
Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). 
Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. 
The boilerplate includes commands to prepare the data.
For each chart, make sure to use a copy of the data frame.

The boilerplate also includes commands to save and return the image.



"""









# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index('date', inplace=True)


df2 = df.copy()

df2 = df2[(df2['value'] > df2['value'].quantile(0.025)) & (df2['value'] < df2['value'].quantile(0.975))]

print(df2)




# Clean data
df = None


def draw_line_plot():
    # Draw line plot





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





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





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
