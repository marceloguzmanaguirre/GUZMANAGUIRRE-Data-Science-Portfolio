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

# Load data
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

# Feature selection
features = st.multiselect("Select features", df.columns.tolist(), default=df.columns.tolist())
if len(features) < 2:
    st.warning("Select at least 2 features.")
    st.stop()

X = df[features]

# Preprocessing data - Allows for categorical data

X = pd.get_dummies(X, drop_first=True)
X = X.dropna()

if X.empty:
    st.error("Selected features result in an empty dataset after encoding. Please choose valid features.")
    st.stop()

X = X.dropna()
X_scaled = StandardScaler().fit_transform(X)


st.sidebar.header("🧠 Model & Hyperparameters 🎚️")
model_type = st.sidebar.selectbox("Choose model", ["KMeans", "PCA", "Hierarchical Clustering"])
train_button = st.button("🚀 Train Model")

if model_type == "KMeans":
    st.subheader("🐑 KMeans Clustering")

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
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)
        df_vis = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
        df_vis["Cluster"] = labels

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

        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)
        df_vis = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
        df_vis["Cluster"] = labels

        fig4, ax4 = plt.subplots(figsize=(13, 5))
        sns.scatterplot(data=df_vis, x="PC1", y="PC2", hue="Cluster", palette="Set1", ax=ax4)
        ax4.set_title("Hierarchical Clustering (PCA Projection)")
        st.pyplot(fig4)

        # Dendrogram
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
        # Fit PCA
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