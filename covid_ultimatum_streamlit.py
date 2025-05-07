import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import calendar

st.set_page_config(
    page_title="Covid Analysis Dashboard",
    page_icon='icons8-covid-19-48.png',

)
data_df = pd.read_csv('./data/ultimatum_covid_file.csv')
data_df['date'] = pd.to_datetime(data_df['date'])
continent_value_counts = data_df['continent'].value_counts()
continent_value_counts = continent_value_counts.reset_index()
continent_value_counts.columns = ['Continent', 'Count']
year_list_value_counts = data_df['year'].value_counts()
year_list_value_counts = year_list_value_counts.reset_index()
year_list_value_counts.columns = ['Year', 'Count']


# st.logo('icons8-covid-19-48.png')
with st.sidebar:
    image = Image.open('covid-19.png')
    original_width, original_height =image.size
    new_height = 120
    new_width = int(original_width * new_height / original_width)
    resized_img = image.resize((new_height, new_height))
    st.image(resized_img)
    # new_image = image.resize((220,600))
    st.title("Covid Analysis SideBar :  ")

    # need to integrate mapping for this
    continent_selected = st.selectbox(label="Select Continent to View Covid", options=continent_value_counts['Continent'], index=None, placeholder='Continent')


    # display location|countries|regions based on continent selected
    location_based_continent_selected = data_df[data_df['continent'] == continent_selected]
    location_name_selected = st.selectbox(label="Select Location/Country in the Given Continent", options=location_based_continent_selected['location'].unique(), index=None, placeholder='Location')

    year_selected = st.selectbox(label='Select year', index=None, options=year_list_value_counts['Year'], placeholder='Year' )

    # location_name = st.selectbox(label="Select Continent to View Covid", placeholder="--Choose--", options=continent_value_counts['Continent']

    interesting_columns = ['total_deaths', 'new_cases', 'new_deaths', 'positive_rate', 'total_vaccinations']
    column_selected = st.selectbox(label="Select column name to view analysis for the data: ", index=None,  options=interesting_columns, placeholder="Select columns")




st.title("Covid Analysis View")




# view for the user:
if  continent_selected != None and location_name_selected != None and year_selected != None and column_selected == None:
    st.subheader('Displaying data for the given continent: ' + continent_selected, divider=True) #  
    st.subheader('Displaying data for the given location : ' + location_name_selected, divider=True) #  
    st.subheader('Displaying data for the given year : ' + str(year_selected), divider=True) #     
    st.subheader('No Column selected:') # 
    # data_df


    continent_filtered_data = data_df[data_df['continent'] == continent_selected].reset_index(drop=True)

    continent_location_filtered_data = continent_filtered_data[continent_filtered_data['location'] == location_name_selected].reset_index(drop=True)
    continent_location__year_filtered_data = continent_location_filtered_data[continent_location_filtered_data['year'] == year_selected]

    st.text(f"The total number of cases for the year: {year_selected} ")
    # plot data for the given year 
    # print(calendar.month) # return object memory location
    month_order = list(calendar.month_name)[1: ] 
    continent_location__year_filtered_data['month'] = continent_location__year_filtered_data['date'].dt.month
    continent_location__year_filtered_data['month_name'] = continent_location__year_filtered_data['date'].dt.strftime("%B")

    # reorganizing the months in the column month_name
    continent_location__year_filtered_data['month_name'] = pd.Categorical(
        continent_location__year_filtered_data['month_name'],
        categories=month_order,
        ordered=True
    )

    # st.text(continent_location__year_filtered_data.groupby('month')['total_cases'].max())

    continent_location_max = continent_location__year_filtered_data.groupby('month_name')['total_cases'].max()
    # st.text(type(continent_location_max))

    continent_location_max = continent_location_max.reset_index()
    continent_location_max.columns = ['Month_Name', 'Total_Cases']
    # get january maximum case
    # st.text(continent_location__year_filtered_data[continent_location__year_filtered_data['month'] == 1]['total_cases'].max())


    "### **Total_Cases Bar Plot**" 
    st.text(f"Continent: {continent_selected} \nLocation:  {location_name_selected} \nYear : {year_selected} \n Selected_Column: {column_selected}")
    st.bar_chart(data=continent_location_max, x='Month_Name', y="Total_Cases")

    
    "### **Total_Deaths Bar Plot**" 
    death_continent_location_max = continent_location__year_filtered_data.groupby('month_name')['total_deaths'].max()
    # st.text(death_continent_location_max)
    death_continent_location_max = death_continent_location_max.reset_index()
    death_continent_location_max.columns = ['Month_Name', 'Total_deaths']
    # death_continent_location_max
    # st.text(f"Continent: {continent_selected} \nLocation:  {location_name_selected} \nYeasr : {year_selected} \n Selected_Column: {column_selected}")
    st.bar_chart(data=death_continent_location_max, x='Month_Name', y="Total_deaths")

    "### **Positive_Rate Bar Plot**" 
    positive_rate_continent_location_max = continent_location__year_filtered_data.groupby('month_name')['positive_rate'].max()
    # st.text(death_continent_location_max)
    positive_rate_continent_location_max = positive_rate_continent_location_max.reset_index()
    positive_rate_continent_location_max.columns = ['Month_Name', 'positive_rate']
    # positive_rate_continent_location_max
    # death_continent_location_max
    # st.text(f"Continent: {continent_selected} \nLocation:  {location_name_selected} \nYeasr : {year_selected} \n Selected_Column: {column_selected}")
    st.bar_chart(data=positive_rate_continent_location_max, x='Month_Name', y="positive_rate")


    "### total_vaccinations Bar Plot"
    total_vaccinations_continent_location_max = continent_location__year_filtered_data.groupby('month_name')['total_vaccinations'].max()
    # st.text(death_continent_location_max)
    total_vaccinations_continent_location_max = total_vaccinations_continent_location_max.reset_index()
    total_vaccinations_continent_location_max.columns = ['Month_Name', 'total_vaccinations']
    # total_vaccinations_continent_location_max

    # st.text(f"Continent: {continent_selected} \nLocation:  {location_name_selected} \nYeasr : {year_selected} \n Selected_Column: {column_selected}")
    st.bar_chart(data=total_vaccinations_continent_location_max, x='Month_Name', y="total_vaccinations")

    "### New_deaths Bar Plot"
    new_deaths_continent_location_max = continent_location__year_filtered_data.groupby('month_name')['new_deaths'].max()
    # st.text(death_continent_location_max)
    new_deaths_continent_location_max = new_deaths_continent_location_max.reset_index()
    new_deaths_continent_location_max.columns = ['Month_Name', 'New_Deaths']
    # total_vaccinations_continent_location_max

    # st.text(f"Continent: {continent_selected} \nLocation:  {location_name_selected} \nYeasr : {year_selected} \n Selected_Column: {column_selected}")
    st.bar_chart(data=new_deaths_continent_location_max, x='Month_Name', y="New_Deaths")


elif continent_selected != None and location_name_selected != None and year_selected != None and column_selected != None:
    st.subheader('Displaying data for the given continent: ' + continent_selected, divider=True) #  
    st.subheader('Displaying data for the given location : ' + location_name_selected, divider=True) #  
    st.subheader('Displaying data for the given year : ' + str(year_selected), divider=True) #     
    st.subheader('Column selected:' + column_selected, divider=True) # 

    continent_filtered_data = data_df[data_df['continent'] == continent_selected].reset_index(drop=True)
 

    continent_location_filtered_data = continent_filtered_data[continent_filtered_data['location'] == location_name_selected].reset_index(drop=True)
    continent_location__year_filtered_data = continent_location_filtered_data[continent_location_filtered_data['year'] == year_selected]


    # plot data for the given year 
    continent_location__year_filtered_data['month'] = continent_location__year_filtered_data['date'].dt.month
    continent_location__year_filtered_data['month_name'] = continent_location__year_filtered_data['date'].dt.strftime("%B")

    # print(calendar.month) # return object memory location
    month_order = list(calendar.month_name)[1: ] 
    # reorganizing the months in the column month_name
    continent_location__year_filtered_data['month_name'] = pd.Categorical(
        continent_location__year_filtered_data['month_name'],
        categories=month_order,
        ordered=True
    )

    # st.text(continent_location__year_filtered_data.groupby('month')['total_cases'].max())

    continent_location_max = continent_location__year_filtered_data.groupby('month_name')[column_selected].max()
    # st.text(type(continent_location_max))

    continent_location_max = continent_location_max.reset_index()
    continent_location_max.columns = ['Month_Name', column_selected]
    # get january maximum case
    # st.text(continent_location__year_filtered_data[continent_location__year_filtered_data['month'] == 1]['total_cases'].max())


    st.subheader(column_selected + " Bar Plot")
    st.text(f"Continent: {continent_selected} \nLocation:  {location_name_selected} \nYear : {year_selected} \n Selected_Column: {column_selected}")

    st.bar_chart(data=continent_location_max, x='Month_Name', y=column_selected)

    continent_location_max
else:
    st.write(" User View Establishing!!! \nPlease fill the first 3 columns")
    st.write("For more insights or detailed information select column from the given options")


