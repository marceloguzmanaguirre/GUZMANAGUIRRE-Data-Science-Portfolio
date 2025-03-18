# 📊 TidyData Project 📈

<em>This repository contains my work for the Tidy Data Project, where I dive into federal research and development spending data from 1976 to 2017, exploring how different government departments have allocated resources as a percentage of GDP over time.</em>

___

## 🔍 Dataset

The dataset `fed_rd_yeargdp.csv` contains:
- 🏢 Department names across federal agencies
- 💵 R&D spending by year with embedded GDP values
- 📆 Data spanning from 1976 to 2017
- 📊 Multiple variables requiring restructuring

___

## 🎯 Project Goals

- 🧹 Clean and transform the data following tidy data principles
- 📈 Create visualizations to explore spending patterns
- 🔄 Apply melting techniques to restructure wide-format data
- 📊 Analyze trends using aggregation functions
- 🧠 Practice real-world data science workflow

___

## ✨ Tidy Data Principles Applied

<details><summary>Each variable in its own column</summary>
  <p>Restructuring data so that year, department, spending, and GDP exist as separate columns rather than embedded in column names.</p>
</details>

<details><summary>Each observation in its own row</summary>
  <p>Transforming the wide format to ensure each department-year combination has its own row.</p>
</details>

<details><summary>Each type of observational unit in its own table</summary>
  <p>Maintaining proper separation of data concepts to ensure analytical clarity.</p>
</details>

___

## 🛠️ Technologies Used

- 🐍 Python - Core programming language
- 🐼 Pandas - Data manipulation and analysis
- 📊 Matplotlib/Seaborn - Data visualization
- 📓 Jupyter Notebook - Interactive coding environment

___

## 📝 Process Overview

1. **Data Exploration** - Understanding the structure and contents
2. **Data Transformation** - Applying melting operations
3. **Data Cleaning** - Extracting embedded information
4. **Visualization** - Creating insightful charts and graphs
5. **Analysis** - Drawing conclusions from the cleaned data

___

## 🔮 Future Work

This project establishes a foundation for further analysis of government spending patterns, potentially exploring:
- Correlation with economic indicators
- Department-specific trend analysis
- Comparative spending across political administrations
