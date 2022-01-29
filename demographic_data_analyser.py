import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df =pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_dict ={}
    for race in df["race"]:
      if race in race_dict:
        race_dict[race] +=1
      else:
        race_dict[race] = 1

      race_count = len(race_dict)


    # What is the average age of men?
    male_df = df["sex"] == "male"
    age_column = male_df["age"]
    average_age_men = age_column.mean()

    # What is the percentage of people who have a Bachelor's degree?
    
    total = len(df["education"])
    bachelor_df = df["education"] == "Bachelors"
    percentage_bachelors = (bachelor_df / total) * 100
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    titles = ["Bachelors", "Masters", "Doctorate"] 
    masters_or_bachelors_df = df[df.education.isin(titles)]
    total = len(masters_or_bachelors_df)

    rich_df = masters_or_bachelors_df["salary"] > 50
    
    percentage_advanced_education = (len(rich_df)/total)*100

    # What percentage of people without advanced education make more than 50K?
   
    no_advanced_ed_df = df[~df.education.isin(titles)]
    total = len(no_advanced_ed_df)
    more_than_50 = df[no_advanced_ed_df["salary"] > 50]
    percentage_without_advanced_education = (len(more_than_50)/total)*100


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    total = len(df)

    higher_education = (len(masters_or_bachelors_df)/total) *100
    lower_education = (len(no_advanced_ed_df)/total)*100


    # percentage with salary >50K
    
    higher_education_rich = (len(df["salary"] > 50)/len(df)) *100
    lower_education_rich = 100 - higher_education_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = pd.min(df["hours-per-week"])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  
    num_min_workers_df = df["hours-per-week"] == min_work_hours

    num_min_workers= len(num_min_workers_df)

    rich_df = num_min_workers_df["salary"] > 50

    rich_percentage = (len(rich_df)/num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    richest_df = df["salary"] > 50

    country_dict = {}
    for country in richest_df:
      country = richest_df["native-country"]
      if country in country_dict:
          country_dict[country] +=1
      else:
        country_dict[country] = 1
    
    highest_earning_country = max(country_dict, key=country_dict.get)
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    country = ["India"]
    india_df = richest_df.native-country.isin(country)

    occupation_dict = {}
    for occupation in india_df:
      occupation = india_df["occupation"]
      if occupation in occupation_dict:
          occupation_dict[occupation] +=1
      else:
        occupation_dict[occupation] = 1

      popular_occupation = max(occupation_dict, key=occupation_dict.get)
    
    
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINEmax(country_dict, key=country_dict.get)

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
