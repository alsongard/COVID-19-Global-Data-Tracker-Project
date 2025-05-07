import pandas as pd
import seaborn as sns

data_df = pd.read_csv('./data/covid_clean_trusted_data.csv')
# print(data_df)

# group data based on continent to get 

# get total_deaths per year
# get total_deaths

print(data_df['date'].dtype) # returns object # 

# convert to datatime
data_df['date'] = pd.to_datetime(data_df['date'])


print(data_df['date'].dtype) # returns datetime64[ns]


# extract the year
data_df['year'] = data_df['date'].dt.year

print(data_df['year'].value_counts())



"""
after getting year column where we have 4 years: 
year
2020    90982
2021    95088
2022    94932
2023    93831
2024    54602

we extract  a dataframe for the given year
from the above results you can make observations on total_cases
"""

covid_2020_data_df = data_df[data_df['year'] == 2020]
# print(covid_2020_data_df)

covid_2021_data_df = data_df[data_df['year'] == 2021]
# print(covid_2021_data_df)

covid_2022_data_df = data_df[data_df['year'] == 2022]
# print(covid_2022_data_df)

covid_2023_data_df = data_df[data_df['year'] == 2023]
# print(covid_2023_data_df)




covid_2024_data_df = data_df[data_df['year'] == 2024]
# print(covid_2024_data_df)



# plot a pie chart or a bar chart depending on the year
# values being pie chart

# print(data_df['total_cases'].isna().sum())


# use 2020 dataframe
covid_2020_data_df['month'] =  covid_2020_data_df['date'].dt.month
print(covid_2020_data_df['month'].value_counts())

covid_2020_total_monthly_cases = covid_2020_data_df.groupby('month')['total_cases'].max()
print(covid_2020_total_monthly_cases)