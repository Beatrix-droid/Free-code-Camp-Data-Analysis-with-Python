import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])

# Clean data
df=df[(df['value'] >= (df['value'].quantile(0.025))) & (df['value'] <= (df['value'].quantile(0.975)))] 



def draw_line_plot():
    ypoints = np.array(df['value'])
    fig=plt.figure(figsize=(15,7))
  
    plt.plot_date(x=df["date"], y=ypoints, color = 'r', linestyle="solid", linewidth=1, markersize=1)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontdict=None, loc='center')
  
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
    # Draw line plot


def draw_bar_plot():
   # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    #caprsint the date time objects and sorting teh months and columns
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%b') for d in df_bar.date]
    df_bar["num"]=[d.month for d in df_bar.date]
    
    #grouping the dataframe
    new_df =df_bar.groupby(["year", "month","num"])["value"].mean().to_frame(name = 'count').reset_index()

    #sorting the months
    sorted_df = new_df.sort_values(by=['num'], ascending=True)
    sorted_df.drop("num", axis=1, inplace=True)
    
  # Draw bar plot
    fig=sns.barplot(data=sorted_df, x=sorted_df["year"], y=sorted_df["count"], hue=sorted_df["month"])
    fig.set(xlabel='Average Page Views', ylabel="Years")
    plt.legend()

    # Save image and return fig (don't change this part)
    fig.figure.savefig('bar_plot.png')
    return fig

def draw_box_plot():
 # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box["num"]=[d.month for d in df_box.date]


    # Draw box plots (using Seaborn)
        #grouping the dataframe as before
    new_df=df_box.groupby(["year", "month","num"],group_keys=True)["value"].apply(lambda x: x).to_frame(name = 'count').reset_index()

    #sorting the months
    sorted_df = new_df.sort_values(by=['num'], ascending=True)
    sorted_df.drop("num", axis=1, inplace=True)

    #prepare for box plot
    sorted_df.rename(columns={'month': 'Month', 'year': 'Year', "count": "Page Views"}, inplace=True)

    fig, axes = plt.subplots(1, 2, sharey=True, figsize=(20,12))
    axes[0].set_title("Year-wise Box Plot (Trend)")
    sns.boxplot(ax=axes[0], data=sorted_df, x='Year', y='Page Views')
    sns.boxplot(ax=axes[1], data=sorted_df, x='Month', y='Page Views')
    sns.despine()
    sns.despine(bottom=True)

    axes[1].set_title("Month-wise Box Plot (Seasonality)")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
