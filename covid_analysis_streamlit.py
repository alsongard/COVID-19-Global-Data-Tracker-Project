import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"# COVID DATA EXPLORATORY ANALYSIS AND PLOTTING"

data_df = pd.read_csv('./data/covid_clean_trusted_data.csv')
data_df

# group data based on continent to get 

# get total_deaths per year
# get total_deaths

# st.write(data_df['date'].dtype) # returns object # 

# convert to datatime
data_df['date'] = pd.to_datetime(data_df['date'])


# st.write(data_df['date'].dtype) # returns datetime64[ns]


# extract the year
'the number of years we have in  our dataset.'
data_df['year'] = data_df['date'].dt.year


'Number of observation we have in each year.'
st.write(data_df['year'].value_counts())




# after getting year column where we have 4 years: 
# year
# 2020    90982
# 2021    95088
# 2022    94932
# 2023    93831
# 2024    54602

# we extract  a dataframe for the given year
# from the above results you can make observations on total_cases
# """





"""
### **Columns Descriptions**

| Variable                     |Description                                                                                                                                                                                                                             |
|:-----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `iso_code`                   | ISO 3166-1 alpha-3 – three-letter country codes. Note that OWID-defined regions (e.g. continents like 'Europe') contain prefix 'OWID_'.                                                                                                    |
| `continent`                  | Continent of the geographical location                                                                                                                                                                                                     |
| `location`                   | Geographical location                                                                                                                                                                                                                      |
| `date`                       | Date of observation        |
| `total_cases`                    | Total confirmed cases of COVID-19. Counts can include probable cases, where reported.                                                                                                                  |
| `new_cases`                      | New confirmed cases of COVID-19. Counts can include probable cases, where reported. In rare cases where our source reports a negative daily change due to a data correction, we set this metric to NA. |
| `new_cases_smoothed`             | New confirmed cases of COVID-19 (7-day smoothed). Counts can include probable cases, where reported.                                                                                                   |
| `total_cases_per_million`        | Total confirmed cases of COVID-19 per 1,000,000 people. Counts can include probable cases, where reported.                                                                                             |
| `new_cases_per_million`          | New confirmed cases of COVID-19 per 1,000,000 people. Counts can include probable cases, where reported.                                                                                               |
| `new_cases_smoothed_per_million` | New confirmed cases of COVID-19 (7-day smoothed) per 1,000,000 people. Counts can include probable cases, where reported.                                                                              |
| `total_deaths`                    | Total deaths attributed to COVID-19. Counts can include probable deaths, where reported.                                                                                                                  |
| `new_deaths`                      | New deaths attributed to COVID-19. Counts can include probable deaths, where reported. In rare cases where our source reports a negative daily change due to a data correction, we set this metric to NA. |
| `new_deaths_smoothed`             | New deaths attributed to COVID-19 (7-day smoothed). Counts can include probable deaths, where reported.                                                                                                   |
| `total_deaths_per_million`        | Total deaths attributed to COVID-19 per 1,000,000 people. Counts can include probable deaths, where reported.                                                                                             |
| `new_deaths_per_million`          | New deaths attributed to COVID-19 per 1,000,000 people. Counts can include probable deaths, where reported.                                                                                               |
| `new_deaths_smoothed_per_million` | New deaths attributed to COVID-19 (7-day smoothed) per 1,000,000 people. Counts can include probable deaths, where reported.  |
| `icu_patients`                       | Number of COVID-19 patients in intensive care units (ICUs) on a given day                                                                                 |
| `icu_patients_per_million`           | Number of COVID-19 patients in intensive care units (ICUs) on a given day per 1,000,000 people                                                            |
| `hosp_patients`                      | Number of COVID-19 patients in hospital on a given day                                                                                                    |
| `hosp_patients_per_million`          | Number of COVID-19 patients in hospital on a given day per 1,000,000 people                                                                               |
| `weekly_icu_admissions`              | Number of COVID-19 patients newly admitted to intensive care units (ICUs) in a given week (reporting date and the preceeding 6 days)                      |
| `weekly_icu_admissions_per_million`  | Number of COVID-19 patients newly admitted to intensive care units (ICUs) in a given week per 1,000,000 people (reporting date and the preceeding 6 days) |
| `weekly_hosp_admissions`             | Number of COVID-19 patients newly admitted to hospitals in a given week (reporting date and the preceeding 6 days)                                        |
| `weekly_hosp_admissions_per_million` | Number of COVID-19 patients newly admitted to hospitals in a given week per 1,000,000 people (reporting date and the preceeding 6 days)                   |
| `reproduction_rate` | Real-time estimate of the effective reproduction rate (R) of COVID-19. See https://github.com/crondonm/TrackingR/tree/main/Estimates-Database |
| `total_tests`                     | Total tests for COVID-19                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `new_tests`                       | New tests for COVID-19 (only calculated for consecutive days)                                                                                                                                                                                                                                                                                                                                                                                                         |
| `total_tests_per_thousand`        | Total tests for COVID-19 per 1,000 people                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `new_tests_per_thousand`          | New tests for COVID-19 per 1,000 people                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `new_tests_smoothed`              | New tests for COVID-19 (7-day smoothed). For countries that don't report testing data on a daily basis, we assume that testing changed equally on a daily basis over any periods in which no data was reported. This produces a complete series of daily figures, which is then averaged over a rolling 7-day window                                                                                                                                                  |
| `new_tests_smoothed_per_thousand` | New tests for COVID-19 (7-day smoothed) per 1,000 people                                                                                                                                                                                                                                                                                                                                                                                                              |
| `positive_rate`                   | The share of COVID-19 tests that are positive, given as a rolling 7-day average (this is the inverse of tests_per_case)                                                                                                                                                                                                                                                                                                                                               |
| `tests_per_case`                  | Tests conducted per new confirmed case of COVID-19, given as a rolling 7-day average (this is the inverse of positive_rate)                                                                                                                                                                                                                                                                                                                                           |
| `tests_units`                     | Units used by the location to report its testing data. A country file can't contain mixed units. All metrics concerning testing data use the specified test unit. Valid units are 'people tested' (number of people tested), 'tests performed' (number of tests performed. a single person can be tested more than once in a given day) and 'samples tested' (number of samples tested. In some cases, more than one sample may be required to perform a given test.) |
| `total_tests`                     | Total tests for COVID-19                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `new_tests`                       | New tests for COVID-19 (only calculated for consecutive days)                                                                                                                                                                                                                                                                                                                                                                                                         |
| `total_tests_per_thousand`        | Total tests for COVID-19 per 1,000 people                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `new_tests_per_thousand`          | New tests for COVID-19 per 1,000 people                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `new_tests_smoothed`              | New tests for COVID-19 (7-day smoothed). For countries that don't report testing data on a daily basis, we assume that testing changed equally on a daily basis over any periods in which no data was reported. This produces a complete series of daily figures, which is then averaged over a rolling 7-day window                                                                                                                                                  |
| `new_tests_smoothed_per_thousand` | New tests for COVID-19 (7-day smoothed) per 1,000 people                                                                                                                                                                                                                                                                                                                                                                                                              |
| `positive_rate`                   | The share of COVID-19 tests that are positive, given as a rolling 7-day average (this is the inverse of tests_per_case)                                                                                                                                                                                                                                                                                                                                               |
| `tests_per_case`                  | Tests conducted per new confirmed case of COVID-19, given as a rolling 7-day average (this is the inverse of positive_rate)                                                                                                                                                                                                                                                                                                                                           |
| `tests_units`                     | Units used by the location to report its testing data. A country file can't contain mixed units. All metrics concerning testing data use the specified test unit. Valid units are 'people tested' (number of people tested), 'tests performed' (number of tests performed. a single person can be tested more than once in a given day) and 'samples tested' (number of samples tested. In some cases, more than one sample may be required to perform a given test.) |
| `population`                 | Population (latest available values). See https://github.com/owid/covid-19-data/blob/master/scripts/input/un/population_latest.csv for full list of sources                                                                                |
| `population_density`         | Number of people divided by land area, measured in square kilometers, most recent year available                                                                                                                                           |
| `median_age`                 | Median age of the population, UN projection for 2020                                                                                                                                                                                       |
| `aged_65_older`              | Share of the population that is 65 years and older, most recent year available                                                                                                                                                             |
| `aged_70_older`              | Share of the population that is 70 years and older in 2015                                                                                                                                                                                 |
| `gdp_per_capita`             | Gross domestic product at purchasing power parity (constant 2011 international dollars), most recent year available                                                                                                                        |
| `extreme_poverty`            | Share of the population living in extreme poverty, most recent year available since 2010                                                                                                                                                   |
| `cardiovasc_death_rate`      | Death rate from cardiovascular disease in 2017 (annual number of deaths per 100,000 people)                                                                                                                                                |
| `diabetes_prevalence`        | Diabetes prevalence (% of population aged 20 to 79) in 2017                                                                                                                                                                                |
| `female_smokers`             | Share of women who smoke, most recent year available                                                                                                                                                                                       |
| `male_smokers`               | Share of men who smoke, most recent year available                                                                                                                                                                                         |
| `handwashing_facilities`     | Share of the population with basic handwashing facilities on premises, most recent year available                                                                                                                                          |
| `hospital_beds_per_thousand` | Hospital beds per 1,000 people, most recent year available since 2010                                                                                                                                                                      |
| `life_expectancy`            | Life expectancy at birth in 2019                                                                                                                                                                                                           |
| `human_development_index`    | A composite index measuring average achievement in three basic dimensions of human development—a long and healthy life, knowledge and a decent standard of living. Values for 2019, imported from http://hdr.undp.org/en/indicators/137506 |



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


"# 2020 Covid Data Analysis"
# add new month column to 2020
covid_2020_data_df['month'] = covid_2020_data_df['date'].dt.month
# st.text(covid_2020_data_df['month'].value_counts()) # this results in the total number of observations for each point
total_cases_for_each_month = covid_2020_data_df.groupby('month')['total_cases'].max()
total_cases_for_each_month
# st.text(type(total_cases_for_each_month))

# convert into a pandas dataframe: total_cases_for_each_month
total_cases_for_each_month = total_cases_for_each_month.reset_index()
total_cases_for_each_month.columns = ['Month', 'MaximumCase']
total_cases_for_each_month


st.bar_chart(data=total_cases_for_each_month, x='Month', y='MaximumCase')
plt.show()
# covid_2020_total_monthly_cases = covid_2020_data_df.groupby('month')['total_cases'].max()
# st.write(covid_2020_total_monthly_cases)


# covid_2020_data_df[covid_2020_data_df['month'] == 1]['total_cases']

# 422750	2032
# 422751	2032
# 422752	2032
# 422753	2032
# 422754	2032
# 422755	2032

# january_cases_df = covid_2020_data_df[covid_2020_data_df['month'] == 1]
# january_cases_df
# st.text(january_cases_df['total_cases'].max())
# january_cases_df.loc[]
# covid_2020_data_df.iloc[422750]


# plot for each month in 2020 year

# covid_2020_data_df.groupby('month')['total_cases'].max()


# st.text()

continent_value_counts = data_df['continent'].value_counts()
continent_value_counts = continent_value_counts.reset_index()
continent_value_counts.columns = ['Continent', 'Count']
continent_value_counts['Continent']

# data_df.to_csv('ultimatum_covid_file.csv', index=False)