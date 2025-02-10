# NYC Air Quality Database Explorer

## Overview
This interactive web application provides a user-friendly interface to explore and analyze New York City's air quality data. Built with Streamlit and Pandas, it offers comprehensive filtering capabilities to help users understand air quality measurements across different locations and time periods.

## Features
- **Air Quality Indicator Selection**: Filter data by specific types of air quality measurements
- **Location-based Filtering**: View data for specific areas within NYC
- **Time Period Selection**: Analyze data from different time periods
- **Value Range Filtering**: Focus on measurements within specific ranges
- **Dynamic Data Display**: Real-time updates of filtered results with measurement counts

## How to Use
1. **Select Air Quality Indicator**: Choose a specific type of measurement or view all indicators
2. **Choose Location**: Filter data by specific NYC locations
3. **Select Time Period**: View data from your chosen time frame
4. **Adjust Value Range**: Use the slider to focus on specific measurement ranges
5. **View Results**: See the filtered data and total number of matching measurements

## Data Source
"Air pollution is one of the most important environmental threats to urban populations and while all people are exposed, pollutant emissions, levels of exposure, and population vulnerability vary across neighborhoods. Exposures to common air pollutants have been linked to respiratory and cardiovascular diseases, cancers, and premature deaths." - United States Government's open data site

## Requirements
- Python
- Streamlit
- Pandas
- Air_Quality.csv dataset

## Getting Started
To run the Air Quality Explorer app:
1. Clone this repository to your local machine
2. Navigate to the GUZMANAGUIRRE-Data-Science-Portfolio directory in your terminal
3. Install required packages: streamlit and pandas using "pip install streamlit pandas"
4. Ensure proper file structure:
 - basic_streamlit_app folder should contain:
   - data folder with Air_Quality.csv inside
   - main.py file
5. Run the app: Use "streamlit run basic_streamlit_app/main.py"
6. Access the app: It will open automatically in your browser