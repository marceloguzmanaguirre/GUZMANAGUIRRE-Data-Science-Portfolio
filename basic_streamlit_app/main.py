import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("data/Air_Quality.csv")
data = df

# Seting up app's title and description
st.title("NYC Air Quality Database")
st.write("This app allows you to explore NYC Air Quality data with interactive filtering options.")

# Dropdown Name (air quality indicators)
name = st.selectbox("Select Air Quality Indicator:", options=["All"] + list(data["Name"].unique()))

# Filtering data based on Name selection
filtered_data = data if name == "All" else data[data["Name"] == name]

# Dropdown for locations
locations = st.selectbox("Select Location:", options=["All"] + list(filtered_data["Geo Place Name"].unique()))

# Filtering data based on location selection
filtered_data = filtered_data if locations == "All" else filtered_data[filtered_data["Geo Place Name"] == locations]

# Filtering time period
time_periods = sorted(list(filtered_data["Time Period"].unique()))
selected_time_period = st.selectbox("Select Time Period:", options=["All"] + time_periods)

# Filtering data based on time period selection
filtered_data = filtered_data if selected_time_period == "All" else filtered_data[filtered_data["Time Period"] == selected_time_period]

# Data Value range slider
min_value, max_value = float(data["Data Value"].min()), float(data["Data Value"].max())
data_value_range = st.slider(
   "Select Data Value range:",
   min_value=min_value,
   max_value=max_value,
   value=(min_value, max_value)
)
filtered_data = filtered_data[
   (filtered_data["Data Value"] >= data_value_range[0]) &
   (filtered_data["Data Value"] <= data_value_range[1])
]

# Displaying filtered data and count
st.subheader(f"There are {len(filtered_data)} measurements that match your specifications")
st.dataframe(filtered_data)