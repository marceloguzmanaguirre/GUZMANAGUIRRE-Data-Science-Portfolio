## Unsupervised Machine Learning App 🧠

<em>This folder contains my interactive unsupervised machine learning application, developed using Python and Streamlit, as part of the "Introduction to Data Science" final project at the University of Notre Dame (Spring 2025). This app allows users to explore unlabeled data through clustering algorithms and dimensionality reduction techniques, with interactive visualizations and parameter tuning capabilities. The project demonstrates core concepts in unsupervised learning, data exploration, and intuitive user interface design.</em>

___

### Project Overview 🔍

The goal of this project is to provide an intuitive and visual platform for exploring unsupervised machine learning techniques. The app supports KMeans clustering, Hierarchical Clustering, and Principal Component Analysis.

![Project Overview](https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/37f000191e153fa33b884de303228bffb510accf/MLUnsupervisedApp/MLUScreenshot.png)

This project enhances my understanding of pattern recognition, clustering algorithms, and dimensionality reduction techniques while developing interactive data science applications.

___

### Instructions 🧭

To run this app locally:

1. Clone this repository
2. Install the required Python packages (pip install -r requirements.txt)
3. Run the Streamlit app (streamlit run unsupervised_app.py)
4. Alternatively, view the deployed version here:

➡️ [Live Streamlit App](https://guzmanaguirre-data-science-portfolio-aagdcxm22d9e7kclumhtgr.streamlit.app/)

___

![App Features](https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/37f000191e153fa33b884de303228bffb510accf/MLUnsupervisedApp/MLUFeatures.png)

___

### Data Visualizations 📊

<details><summary>KMeans Clustering - Elbow Plot</summary>
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/37f000191e153fa33b884de303228bffb510accf/MLUnsupervisedApp/MLUElbow.png"/>
This plot helps identify the optimal number of clusters by showing the point where adding more clusters provides diminishing returns. The "elbow" in the curve represents the ideal balance between simplicity and accuracy.
</details>

<details><summary>PCA-Based Cluster Visualization</summary>
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/37f000191e153fa33b884de303228bffb510accf/MLUnsupervisedApp/MLUPCA.png"/>
This scatterplot shows the clustering results projected onto the first two principal components, making it possible to visualize high-dimensional clusters in a 2D space. Different colors represent distinct clusters identified by the algorithm.
</details>

<details><summary>Hierarchical Clustering Dendrogram</summary>
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/37f000191e153fa33b884de303228bffb510accf/MLUnsupervisedApp/MLUDendogram.png"/>
The dendrogram visualizes the hierarchical relationship between clusters, showing how data points are grouped together at different similarity levels. The height of each branch represents the distance between merged clusters.
</details>

<details><summary>PCA Explained Variance</summary>
<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/37f000191e153fa33b884de303228bffb510accf/MLUnsupervisedApp/MLUVariance.png"/>
This bar chart illustrates how much information each principal component captures, helping users understand how effectively the dimensionality reduction preserves the original data's structure and variance.
</details>

___

### Technical Implementation 🛠️

This application leverages several key Python libraries:

- **Streamlit**: Powers the interactive web interface
- **Scikit-learn**: Provides machine learning algorithms (KMeans, PCA, AgglomerativeClustering)
- **Pandas**: Handles data manipulation and preprocessing
- **Matplotlib & Seaborn**: Generate detailed visualizations
- **NumPy**: Supports numerical operations and data transformations

The app implements a responsive design that guides users through the unsupervised learning workflow:

1. Data selection and feature engineering
2. Algorithm selection and parameter tuning
3. Model training with performance metrics
4. Interactive result visualization and interpretation

___

<img src="https://github.com/marceloguzmanaguirre/GUZMANAGUIRRE-Data-Science-Portfolio/blob/201831ead0d322ef8bfb941e5faaf754cc82bc36/MLUnsupervisedApp/MLULearningOutcomes.png"/>

___

### Future Enhancements 🚀

- Add DBSCAN and other density-based clustering algorithms
- Implement t-SNE visualization for high-dimensional data
- Add cluster validation metrics beyond silhouette score
- Create interactive 3D visualization options for PCA results
- Enable saving and exporting of trained models and results
