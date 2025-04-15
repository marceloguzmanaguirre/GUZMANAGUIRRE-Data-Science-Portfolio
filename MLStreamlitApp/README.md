## This is my Streamlit ML App Repository! 🤖
<em>This repository contains my interactive machine learning application, developed using Python and Streamlit, as part of the "Introduction to Data Science" course at the University of Notre Dame (Spring 2025). This app allows users to upload their own datasets, select machine learning models, tune hyperparameters, and visualize performance metrics. The project reflects core concepts in supervised learning, model interpretability, and user-friendly deployment.</em>
___
### Project Overview 🧑🏻
The goal of this project is to provide an interactive and visual experience for supervised machine learning. The app supports both Decision Tree and Logistic Regression classifiers. 

<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/main/MLStreamlitApp/1.png"/>

This project strengthens my understanding of data preprocessing, modeling, and interactive app development with Streamlit.

___
### Instructions 🧭
To run this app locally:

1. Clone this repository
2. Install the required Python packages (pip install -r requirements.txt)
3. Run the Streamlit app (streamlit run app.py)
4. Alternatively, view the deployed version here:  
➡️ [Live Streamlit App](https://guzmanaguirre-data-science-portfolio-egpxyvdq5txsrvalakeby2.streamlit.app/)
___
### App Features ⚙️
- **Models Used:**
  - Decision Tree Classifier: Max depth is adjustable via a slider.
  - Logistic Regression: Uses default hyperparameters (max_iter = 1000).
- **User Controls:**
  - Select target variable and features
  - Adjust train/test split ratio
  - Visualize results instantly
- **Error Handling:**
  - Ensures target variable is categorical when using classifiers
 
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/main/MLStreamlitApp/2.png"/>
___
### Data Visualizations 📊
- **Confusion Matrix 🧮**: This plot displays the number of correct and incorrect predictions, giving insight into how well the model performs on each class. Especially helpful for classification tasks.
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/main/MLStreamlitApp/3.png"/>

- **Feature Importance 🌲**: For the Decision Tree model, this horizontal bar chart shows which features had the most influence on the model's predictions.
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/main/MLStreamlitApp/4.png"/>

- **Correlation Heatmap 🔗**: Shows the pairwise correlation coefficients between numeric features. Helps identify multicollinearity and understand feature relationships.
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/main/MLStreamlitApp/5.png"/>

- **Histogram + KDE 📈**: This combo plot visualizes the distribution of a selected numeric feature. The histogram shows counts, while the KDE overlay reveals the shape of the distribution.
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/main/MLStreamlitApp/6.png"/>

Each visualization is implemented using Matplotlib and Seaborn in accordance with class formatting.

___
### Visual Examples 🖼️
Below are a few screenshots from the app:

<details><summary>Main Interface</summary>
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/main/MLStreamlitApp/7.png"/>
</details>

<details><summary>Error message to facilitate user engagment with the statistical model</summary>
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/main/MLStreamlitApp/8.png"/>
</details>

