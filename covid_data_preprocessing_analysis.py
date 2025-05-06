
import pandas as pd
import seaborn as sns


data_df = pd.read_csv("./data/owid-covid-data.csv")
print(data_df)

print(data_df.columns)

print(data_df.head(10))


print(data_df.info())


#**Data preprocessing**


print(data_df.shape)

print(f'Rows for the dataset is {data_df.shape[0]}  and  columns are : {data_df.shape[1]}')


# checking for null colums
pd.set_option('display.max_rows', None)
null_counts = data_df.isna().sum()
print(null_counts)



clean_trusted_df = data_df[['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_cases_per_million', 'new_cases_per_million','total_tests','new_tests','positive_rate','tests_per_case','tests_units','total_vaccinations','people_vaccinated','people_fully_vaccinated', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older','male_smokers','female_smokers','human_development_index']]
continent_value_counts = clean_trusted_df['continent'].value_counts()
continent_value_counts = continent_value_counts.reset_index()
continent_value_counts.columns =  ['Continent Name' , 'Counts']
continent_value_counts
value = 0
for item in continent_value_counts['Counts']:
    value+=item
print(value)


pd.set_option('display.max_column', 10, 'display.max_rows', 10)
print(clean_trusted_df)


# checking difference on value counts and missing data
print(429435-402910)

# view empty rows on country
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)
print(clean_trusted_df[clean_trusted_df['continent'].isna()])


null_data_frame_analysis = clean_trusted_df[clean_trusted_df['continent'].isna()]
null_data_frame_analysis


null_data_frame_analysis[null_data_frame_analysis['location'] == 'Africa']

null_data_frame_analysis['location'].value_counts()

clean_trusted_df['continent'] = clean_trusted_df['continent'].fillna(clean_trusted_df['location'])

print(clean_trusted_df['continent'].isna().value_counts())

print(clean_trusted_df.columns)

pd.set_option('display.max_rows', 10)
clean_trusted_df['location'].value_counts()


pd.set_option('display.max_rows', 25)
clean_trusted_df.isna().sum()


## **CONTINUING WITH DATA PREPROCESSING**

# pd.set_option('display.max_column', 10, 'display.max_rows', 10)
# with pd.option_context('display.max_column', 26, 'display.max_rows', 29304):
#     print(clean_trusted_df[clean_trusted_df['total_cases'].isna()])
clean_trusted_df['total_cases'] = clean_trusted_df['total_cases'].fillna(0.0)
clean_trusted_df.shape


pd.set_option('display.max_rows', 26)
clean_trusted_df.isna().sum()


clean_trusted_df['new_cases'].isna().value_counts()


clean_trusted_df.isna().sum()


with pd.option_context('display.max_rows', 19277, 'display.max_column', 26):
    print(clean_trusted_df[clean_trusted_df['new_cases'].isna()])


clean_trusted_df['new_cases'] = clean_trusted_df['new_cases'].fillna(0.0)

clean_trusted_df.isna().sum()


clean_trusted_df[['total_deaths','new_deaths', 'total_cases_per_million','new_cases_per_million', 'total_tests', 'new_tests', 'positive_rate','tests_per_case', 'total_vaccinations','people_vaccinated', 'people_fully_vaccinated','population_density']] = clean_trusted_df[['total_deaths','new_deaths', 'total_cases_per_million','new_cases_per_million', 'total_tests', 'new_tests', 'positive_rate','tests_per_case', 'total_vaccinations','people_vaccinated', 'people_fully_vaccinated','population_density']].fillna(0.0)


with pd.option_context('display.max_rows', 30, 'display.max_columns', 5):
    print(clean_trusted_df.isna().sum())


# droping tests_units row :reason: to may empty rows
clean_trusted_df = clean_trusted_df.drop('tests_units', axis=1)

with pd.option_context('display.max_rows', None):
    clean_trusted_df.info()

clean_trusted_df.isna().sum()


# median_age_value_counts = clean_trusted_df['median_age'].value_counts()
# median_age_value_counts

print('Filling Missing Values')
clean_trusted_df['median_age'] = clean_trusted_df['median_age'].fillna(0.0)
clean_trusted_df['aged_65_older'] = clean_trusted_df['aged_65_older'].fillna(0.0)
clean_trusted_df['aged_70_older'] = clean_trusted_df['aged_70_older'].fillna(0.0)

clean_trusted_df = clean_trusted_df.drop(columns=['male_smokers', 'female_smokers', 'human_development_index'], axis=1)
print(clean_trusted_df)
# clean_trusted_df.info()

# medina_age_value_counts = medina_age_value_counts.reset_index()
# medina_age_value_counts.column = ['category', 'count']
# print(medina_age_value_counts['count'].sum()) #will need to check other columns before dropping rows with missing values on 'median_age'


# age_65_older_values_counts = clean_trusted_df['aged_65_older'].value_counts()
# age_65_older_values_counts = age_65_older_values_counts.reset_index()
# age_65_older_values_counts.column = ['category', 'count']
# print(age_65_older_values_counts['count'].sum())

# """
# aged_70_older               98120
# male_smokers               185618
# female_smokers             182270
# human_development_index    110308
# """

# clean_trusted_df['aged_65_older'].value_counts()
# clean_trusted_df


print(clean_trusted_df.shape)

with pd.option_context('display.max_rows', None, 'display.max_column', None):
    print(clean_trusted_df.isna().sum())


# done with preprocessing

# save file for plotting
clean_trusted_df.to_csv("./data/covid_clean_trusted_data.csv", index=False)