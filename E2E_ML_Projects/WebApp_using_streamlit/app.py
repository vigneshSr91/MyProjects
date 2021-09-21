import streamlit as st
import pandas as pd
import numpy as np

# Add title for the app
st.title('Uber pick ups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(numberOfRows):
    data = pd.read_csv(DATA_URL,nrows=numberOfRows)
    lowercase = lambda x: str(x).lower( )
    data.rename(lowercase,axis='columns',inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading Data....')

data = load_data(10000)

data_load_state.text('Load of Data complete!!')

# Display Raw Data with a checkbox/toggle
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)


# Display a histogram with the Number of Pickups vs time/hour of the day

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# Display a map(geographic location) of pickup information

hourToFilter = st.slider('hour',0,23,17)
filteredData = data[data[DATE_COLUMN].dt.hour == hourToFilter]
st.subheader(f'Map of all pickups at {hourToFilter}:00')
st.map(filteredData)


