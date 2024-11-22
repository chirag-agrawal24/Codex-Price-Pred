# codebasics ML course: codebasics.io, all rights reserverd
import json
import streamlit as st
from price_calculator import calculate

# Define the page layout
st.title('Codex Beverage Price Prediction')

with open("artifacts/column_datas.json") as json_file:
    categorical_options = json.load(json_file)




# We would mimic the structure of actual data given(before feature engineered)
# Create a 4x4 grid layout
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)

# Assign inputs to the grid
input_dict = {}

# First row
with row1[0]:
    input_dict['age'] = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    input_dict['gender'] = st.selectbox('Gender', categorical_options['gender'])
with row1[2]:
    input_dict['zone'] = st.selectbox('Geographical Zone', categorical_options['zone'])
with row1[3]:
    input_dict['occupation'] = st.selectbox('Occupation', categorical_options['occupation'])

# Second row
with row2[0]:
    input_dict['income_levels'] = st.selectbox('Income Range (In Lakhs)', categorical_options['income_levels'])
with row2[1]:
    input_dict['current_brand'] = st.selectbox('Current Brand', categorical_options['current_brand'])
with row2[2]:
    input_dict['awareness_of_other_brands'] = st.selectbox('Awareness of Other Brands', categorical_options['awareness_of_other_brands'])
with row2[3]:
    input_dict['reasons_for_choosing_brands'] = st.selectbox('Choose Codex for', categorical_options['reasons_for_choosing_brands'])

# Third row
with row3[0]:
    input_dict['consume_frequency(weekly)'] = st.selectbox('Consume Frequency (Weekly)', categorical_options['consume_frequency(weekly)'])
with row3[1]:
    input_dict['typical_consumption_situations'] = st.selectbox('Typical Consumption Situations', categorical_options['typical_consumption_situations'])
with row3[2]:
    input_dict['preferable_consumption_size'] = st.selectbox('Size Preference', categorical_options['preferable_consumption_size'])
with row3[3]:
    input_dict['flavor_preference'] = st.selectbox('Flavor Preference', categorical_options['flavor_preference'])
    
# Fourth row
with row4[0]:
    input_dict['health_concerns'] = st.selectbox('Health Concerns', categorical_options['health_concerns'])
with row4[1]:
    input_dict['packaging_preference'] = st.selectbox('Packaging Preference', categorical_options['packaging_preference'])
with row4[2]:
    input_dict['purchase_channel'] = st.selectbox('Purchase Channel', categorical_options['purchase_channel'])


# Button to make prediction
if st.button('Calculate Price Range'):

    #logical erro 
    if input_dict['age']>55 and input_dict['occupation']=="Student":
        st.error("A Student can not be older than 55 Years")
    elif input_dict['age']<40 and input_dict['occupation']=="Retired":
        st.error("Your age does not seems to be Retirement age")

    else:
        price = calculate(input_dict)
        st.success(f'Price Range: {price} INR')
