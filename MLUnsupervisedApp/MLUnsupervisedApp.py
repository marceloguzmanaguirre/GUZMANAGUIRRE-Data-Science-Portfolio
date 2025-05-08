import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Basic Layout
st.set_page_config(page_title="Unsupervised Machine Learning App", layout="wide")
st.title("Unsupervised Machine Learning App")
st.sidebar.header("📁 Data Source")
data_option = st.sidebar.radio("Choose data source:", ["Sample Iris Dataset", "Upload CSV"])

# If the user chooses "Upload CSV," it displays a file uploader in the sidebar that accepts CSV files. When a file is uploaded, it reads the data into a pandas DataFrame; if no file is uploaded, it stops execution. If another data option is selected, it loads the built-in Iris dataset and converts it to a DataFrame with appropriate column names from the original feature name
if data_option == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload your CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.stop()
else:
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)

st.subheader("📄 Dataset Preview")
st.write(df.sample(10))

# I've added a feature selection interface that lets you pick which columns you want to include in your analysis. I used a multiselect dropdown that's initially populated with all the columns from your DataFrame. If user selects fewer than two features, app will show them a warning message and stop execution - this ensures user has enough data to perform a meaningful analysis before moving forward with the app
features = st.multiselect("Select features", df.columns.tolist(), default=df.columns.tolist())
if len(features) < 2:
    st.warning("Select at least 2 features.")
    st.stop()

X = df[features]

# Preprocessing data - Allows for categorical data
# I included code to prepare user data for modeling. First, I convert any categorical features into numeric ones using one-hot encoding with pd.get_dummies(), and I drop the first category to avoid multicollinearity. Then I remove any rows with missing values
# I added a safety check to make sure user's dataset isn't empty after these operations. If it is, it'll show them an error message and stop execution so user can select different features
# After cleaning the data, I standardize all features using StandardScaler() to ensure they're on the same scale. This is important for many machine learning algorithms, especially those that rely on distances between data points or regularization

X = pd.get_dummies(X, drop_first=True)
X = X.dropna()

if X.empty:
    st.error("Selected features result in an empty dataset after encoding. Please choose valid features.")
    st.stop()

X = X.dropna()
X_scaled = StandardScaler().fit_transform(X)

# My app provides an intuitive sidebar interface with a brain emoji header where you can select your preferred unsupervised learning algorithm from three options (KMeans, PCA, or Hierarchical Clustering)
st.sidebar.header("🧠 Model & Hyperparameters 🎚️")
model_type = st.sidebar.selectbox("Choose model", ["KMeans", "PCA", "Hierarchical Clustering"])
train_button = st.button("🚀 Train Model")

if model_type == "KMeans":
    st.subheader("🐑 KMeans Clustering")
    
    # I added a subheader and slider for setting the maximum number of clusters to test in the Elbow Method, allowing user to explore optimal clustering from 3 to 20 groups. I created another subheader with a slider that lets user directly choose how many clusters KMeans will use to divide your data, ranging from 2 up to your selected maximum.
    st.sidebar.subheader("Max Clusters for Elbow plot")
    max_clusters = st.sidebar.slider("Sets the upper limit of clusters to test for optimal k in the Elbow Method", 3, 20, 6)
    st.sidebar.subheader("Max Clusters for KMeans")
    k = st.sidebar.slider("Number of clusters: sets how many groups the algorithm will divide the data into", 2, max_clusters, 3)

    if train_button:
        # Fit User's selected model with K clusters
        model = KMeans(n_clusters=k, random_state=42).fit(X_scaled)
        labels = model.predict(X_scaled)
        st.caption(f"Kmeans completed with {k} clusters.")
        silhouette = silhouette_score(X_scaled, labels)
        st.success(f"Silhouette Score: `{silhouette:.3f}`")
        
        # Find eblow plot values for each k until max_clusters
        sse = []
        for i in range(2, max_clusters + 1):
            km = KMeans(n_clusters=i, random_state=42).fit(X_scaled)
            sse.append(km.inertia_)

        # Plot the elbow k-means values
        st.subheader("📈 Elbow Method")
        st.expander("Elbow Method", expanded=True).markdown(
            """
            The elbow plot is used to find the optimal number of clusters for KMeans. In order to find the optimal number of clusters, 
            we look for the point where the inertia (sum of squared distances to the nearest cluster center) starts to decrease at a slower rate. 
            In simple terms, choose the "k" where the elbow plot shows a sharp bend. After this point, adding more clusters doesn't improve the results.
            """
        )
        
        # I create a wide figure with  Elbow Plot showing how the sum of squared distances (inertia) changes as  number of clusters increases, helping user visually identify the optimal point where adding more clusters provides diminishing returns.
        fig, ax = plt.subplots(figsize=(13,5))
        ax.plot(range(2, max_clusters + 1), sse, marker='o')
        ax.set_title("Elbow Plot")
        ax.set_xlabel("Number of Clusters")
        ax.set_ylabel("Inertia")
        st.pyplot(fig)

        # Visualize using 2 PCA Projection
        st.subheader("📊 PCA Visualization")
        st.expander("PCA Visualization", expanded=True).markdown(
            """
            PCA (Principal Component Analysis) reduces data dimensionality while retaining the most significant variance. 
            This graph shows the clusters formed by KMeans in a 2D space using PCA.
            """
        )
        
        # I reduce the dimensionality of your standardized data to two principal components using PCA, coverting the transformed data into a DataFrame with labeled columns for easier handling, and adds the cluster assignments as a third column to prepare for visualization of how user data naturally groups
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)
        df_vis = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
        df_vis["Cluster"] = labels
        
        # App creates a wide figure (13×5) and set up an axis for plotting. Using seaborn's scatterplot function, I visualize the PCA-transformed data with PC1 on the x-axis, PC2 on the y-axis, and color-code points by their cluster assignments using the Set2 color palette. I display the finished visualization
        fig2, ax2 = plt.subplots(figsize=(13,5))
        sns.scatterplot(data=df_vis, x="PC1", y="PC2", hue="Cluster", palette="Set2", ax=ax2)
        ax2.set_title("Clusters (PCA)")
        st.pyplot(fig2)
elif model_type == "Hierarchical Clustering":
    st.subheader("🌲 Hierarchical Clustering")
    st.sidebar.subheader("Number of Clusters")
    k = st.sidebar.slider("Number of clusters", 2, 10, 3)

    if train_button:
        # Use agglomerative clustering with K clusters
        model = AgglomerativeClustering(n_clusters=k)
        labels = model.fit_predict(X_scaled)
        st.caption(f"Hierarchical Clustering done with {k} clusters.")
        score = silhouette_score(X_scaled, labels)
        st.success(f"Silhouette Score: `{score:.3f}`")

        # Visualize 2 PCA Projection
        st.subheader("📊 PCA Visualization")
        st.expander("PCA Visualization", expanded=True).markdown(
            """
            PCA (Principal Component Analysis) reduces data dimensionality while retaining the most significant variance. 
            This graph shows the clusters formed by KMeans in a 2D space using PCA.
            """
        )
        
        # I apply Principal Component Analysis to reduce user's standardized data to two dimensions, transform the results into a DataFrame with columns labeled "PC1" and "PC2", and add a "Cluster" column containing user's model's cluster assignments to prepare for visualizatio
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)
        df_vis = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
        df_vis["Cluster"] = labels

        # I create a wide scatter plot that visualizes your clustering results by showing the data points projected onto the first two principal components, with different colors representing each cluster assignment
        fig4, ax4 = plt.subplots(figsize=(13, 5))
        sns.scatterplot(data=df_vis, x="PC1", y="PC2", hue="Cluster", palette="Set1", ax=ax4)
        ax4.set_title("Hierarchical Clustering (PCA Projection)")
        st.pyplot(fig4)

        # I add a section for the dendrogram, include an expanded explanation of what dendrograms show in hierarchical clustering, then generate the visualization using Ward's method to display how your data points merge into clusters, with the height representing similarity levels and limiting display to the last 20 merge steps for clarit
        st.subheader("👑 Dendrogram")
        st.expander("Dendrogram Explanation", expanded=True).markdown(
            """
            A dendrogram visualizes the hierarchy of clusters formed by hierarchical clustering. 
            It shows how data points are merged step-by-step, with the height indicating the similarity level between clusters.
            """
        )
        linked = linkage(X_scaled, 'ward')
        fig5, ax5 = plt.subplots(figsize=(13, 5))
        dendrogram(linked, truncate_mode="lastp", p=20, leaf_font_size=10, ax=ax5)
        ax5.set_title("Hierarchical Clustering Dendrogram")
        st.pyplot(fig5)

elif model_type == "PCA":
    st.subheader("📊 Principal Component Analysis")
    st.sidebar.subheader("PCA Components")
    n_components = st.sidebar.slider("Sets how many principal components to keep, reducing data while preserving most variance", 2, min(len(features), 5), 2)

    if train_button:
        # App displays a confirmation message showing the number of principal components user selected, fit a PCA model to standardized data using that specification, transform the data into the new lower-dimensional space, and calculate the percentage of variance explained by each principal component for further analysis
        st.caption(f"PCA completed with {n_components} components.")
        pca = PCA(n_components=n_components)
        X_pca = pca.fit_transform(X_scaled)
        explained_var = pca.explained_variance_ratio_
        
        # Plot explained variance
        st.subheader("📈 Explained Variance")
        st.expander("Explained Variance", expanded=True).markdown(
            """
            Explained variance shows how much information each principal component captures from the data. 
            This bar chart helps you understand how the  contribute tcomponentso the overall variance.
            """
        )
        fig3, ax3 = plt.subplots(figsize=(13,5))
        ax3.bar(range(1, n_components + 1), explained_var * 100)
        ax3.set_title("Explained Variance by Component")
        ax3.set_xlabel("Principal Component")
        ax3.set_ylabel("Variance (%)")
        st.pyplot(fig3)

        # Show PCA output
        st.subheader("📊 PCA Output")
        st.expander("PCA Table", expanded=True).markdown(
            """
            This table shows the transformed data after applying PCA. Each row represents a sample, and each column represents a principal component.
            The values indicate the projection of the original data onto the principal components.
            """
        )
        st.write("PCA Output (first 5 rows):")
        st.dataframe(pd.DataFrame(X_pca, columns=[f"PC{i+1}" for i in range(n_components)]).head())