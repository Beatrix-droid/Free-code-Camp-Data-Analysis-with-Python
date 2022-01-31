import pandas as pd


def calculate_demographic_data(print_data=True):
  
   
    # Read data from file
    df=pd.read_csv("adult.data.csv")
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = df["race"].value_counts()

    # What is the average age of men?
    male_df = df.loc[df["sex"] == "Male", "age"]
    age = male_df.mean()
    average_age_men = age.round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelor_df = df[df["education"] == "Bachelors"]
    percentage_bachelors = round(len(bachelor_df)/ len(df)*100,1)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    titles = ["Bachelors", "Masters", "Doctorate"] 
    masters_or_bachelors_df = df[df.education.isin(titles)]
    uneducated_df = df[~df.education.isin(titles)]
    educated_rich = masters_or_bachelors_df[ masters_or_bachelors_df["salary"] == ">50K"]


    # percentage with salary >50K
    higher_education_rich = round((len(educated_rich)/len(masters_or_bachelors_df)) * 100, 1)
   
    uneducated_rich_df = uneducated_df[uneducated_df["salary"]==">50K"]

    lower_education_rich =  round(len(uneducated_rich_df)/len(uneducated_df)*100, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round((len(educated_rich)/len(df)) * 100, 1)
    lower_education = 100 - higher_education_rich



    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
     
    min_workers_df = df.loc[df["hours-per-week"]== min_work_hours, "salary"]
    rich_df = min_workers_df.loc[min_workers_df == ">50K"]
    
    num_min_workers =  len(min_workers_df)

    rich_percentage = (len(rich_df)/num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    # What country has the highest percentage of people that earn >50K?
    richest_df = df.loc[df["salary"] == ">50K", "native-country"]
    country_dict = {}
    for country in richest_df:
      if country in country_dict:
          country_dict[country] +=1
      else:
        country_dict[country] = 1
    
    
    richest_df = df.loc[df["salary"] == ">50K", "native-country"]
    country_dict = {}
    for country in richest_df:
        if country in country_dict:
            country_dict[country] +=1
        else:
          country_dict[country] = 1
    

    countries= {}
    country_df = df[["salary", "native-country"]]
    for country in country_df["native-country"]:
      if country in countries:
          countries[country]+= 1
      else:
          countries[country] =1
   

    percentages_richest = {}
    for country in country_dict:
      if country in countries:
          percentages_richest[country] = country_dict[country]/countries[country]*100
   
    
    highest_earning_country = max(percentages_richest, key=percentages_richest.get)

    highest_percentage = max(percentages_richest.values())
    highest_earning_country_percentage = round(highest_percentage, 1)


    
    
    # Identify the most popular occupation for those who earn >50K in India.
    India_occupation = {}
    India_df = df.loc[df["native-country"] == "India", "occupation"]
    for occupation in India_df:
      if occupation in India_occupation:
          India_occupation[occupation]+=1
      else:
          India_occupation[occupation]=1
        
    top_IN_occupation= max(India_occupation, key=India_occupation.get)
  
  

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
          'race_count': race_count,
          'average_age_men': average_age_men,
          'percentage_bachelors': percentage_bachelors,
          'higher_education_rich': higher_education_rich,
          'lower_education_rich': lower_education_rich,
          'min_work_hours': min_work_hours,
          'rich_percentage': rich_percentage,
          'highest_earning_country': highest_earning_country,
          'highest_earning_country_percentage':
          highest_earning_country_percentage,
          'top_IN_occupation': top_IN_occupation
        }
