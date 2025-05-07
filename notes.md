# to design your sidebar
```
import streamlit as st

st.sidebar:
    st.title('enter title here')

    # get year_lsit
    year_list = data_df['year'].value_counts

    # the st.select_box() is used to display a select option in which a user can select 
    a list/option from the list
    relevant arguments:
        label (str) : accepts a string similar to <label></label> It displays/shows text informing the user on the use of selectbox
        placeholder: (optional) string that is displayed before any input
        options(Iterable): a list for user to select()
        accept_new_options(bool): whether a user can add a selection/data that isn't in the options iterable
        False: user can only select from the given options
        True: use can add his/her own data
        index(int): hte index of the preselected option on first render. If None, will initialize empty and return None until the user selects an option. Defaults to 0 (the first option).

    country_name = st.selectbox(label="Select Country")

    year_name = st.selectbox(label='Select Year")


    # to display an image and specify it's height
    # use the PIL module
