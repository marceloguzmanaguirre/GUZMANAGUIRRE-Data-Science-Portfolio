# 📊 TidyData Project 📈

<em>This repository contains my work for the Tidy Data Project, where I dive into federal research and development spending data from 1976 to 2017, exploring how different government departments have allocated resources as a percentage of GDP over time.</em>

___

## 🔍 Project Overview
This project applies tidy data principles to transform and analyze a dataset of federal R&D spending. Tidy data follows three key rules:
1. Each variable forms a column
2. Each observation forms a row
3. Each type of observational unit forms a table
By restructuring our dataset to follow these principles, we can more easily analyze spending patterns and trends across different government departments over time.

___

## 📋 Instructions

### Dependencies
To run this notebook, you'll need the following Python libraries:
- pandas
- numpy
- matplotlib
- seaborn

You can install these dependencies using pip:

    pip install pandas numpy matplotlib seaborn

### Running the Notebook
1. Clone this repository:

    git clone https://github.com/yourusername/TidyData-Project.git
    cd TidyData-Project

2. Start Jupyter Notebook:

    jupyter notebook

3. Open the `Federal_RD_Analysis.ipynb` file in your browser

4. Run all cells in sequence (Cell > Run All)

___

## 🔍 Dataset

The dataset `fed_rd_yeargdp.csv` contains:
- 🏢 Department names across federal agencies
- 💵 R&D spending by year with embedded GDP values
- 📆 Data spanning from 1976 to 2017
- 📊 Multiple variables requiring restructuring

### Pre-processing Steps:
- Data was obtained from public government records
- Original format is in "wide" format with years as columns
- GDP values are embedded within column names
- Dataset requires tidying before analysis can begin

___

## 🛠️ Technologies Used

- 🐍 Python - Core programming language
- 🐼 Pandas - Data manipulation and analysis
- 📊 Matplotlib/Seaborn - Data visualization
- 📓 Jupyter Notebook - Interactive coding environment

___

## 📸 Visual Examples

### Data Transformation
![Before and After Tidying](https://placeholder-for-your-image.png)
*Screenshot showing the data before and after the tidying process*

### Key Visualization
![Department Spending Trends](https://placeholder-for-your-visualization.png)
*Visualization of spending trends across top departments*

___

## 📚 References

- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Tidy Data Paper by Hadley Wickham](https://www.jstatsoft.org/article/view/v059i10)
- [Data Wrangling with pandas](https://pandas.pydata.org/docs/user_guide/reshaping.html)
- [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)

___

## 🔮 Future Work

This project establishes a foundation for further analysis of government spending patterns, potentially exploring:
- Correlation with economic indicators
- Department-specific trend analysis
- Comparative spending across political administrations
