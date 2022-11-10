import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
  df = pd.read_csv("epa-sea-level.csv")
  x = df["Year"]
  y = df["CSIRO Adjusted Sea Level"]

  #define points for the second line of best fit
  new_df = df.loc[(df['Year'] >= 2000)]
  x_1 = new_df["Year"]
  y_1 = new_df["CSIRO Adjusted Sea Level"]

  pd_dict = {'Year':[],
        "CSIRO Adjusted Sea Level":[]
       }

  #create the regression for the first line of best fit
  regression = linregress(x, y)
  m = regression.slope
  b = regression.intercept


  #create the regression for the second line of best fit
  regression_2000 = linregress(x_1, y_1)

  #extend the line of best fit to include 2050 by adding new points to the original df
  x_points = np.linspace(2014, 2050, 37 )
  for i in x_points:
    pd_dict["Year"].append(i)
    pd_dict["CSIRO Adjusted Sea Level"].append(i*m+ b)

  df2 = pd.DataFrame(pd_dict)
  df2= pd.concat([df, df2])

  #define the coordiinates fot the first line of best fit:
  x_first = df2["Year"]
  y_first = df2["CSIRO Adjusted Sea Level"]


  pd_dict_2 = {'Year':[],
        "CSIRO Adjusted Sea Level":[]
       }
  for i in x_points:
    pd_dict_2["Year"].append(i)
    pd_dict_2["CSIRO Adjusted Sea Level"].append(i*regression_2000.slope+ regression_2000.intercept)


  df3 = pd.DataFrame(pd_dict_2)
  df3= pd.concat([new_df, df3])

  x_2 = df3["Year"] 

  #plot the scatter plot
  plt.scatter(x, y, s= 1)
  plt.plot(x_first, b + m*x_first, 'r', label='fitted line from 1880 to 2050')
  plt.plot(x_2, regression_2000.intercept + regression_2000.slope*x_2, 'g', label='fitted line from 200 to 2050')
  plt.xlim([1850, 2075])
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
  plt.legend()
    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
