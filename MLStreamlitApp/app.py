import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.utils.multiclass import type_of_target

# Header and a brief description of what the user should do (upload data, choose features, etc.)
st.title("Interactive Supervised Machine Learning App 🧠")
st.write("""
Upload a dataset (or use the sample), choose features and a target, train a model, and explore results visually!
""")

# Sidebar (inludes option for user to use sample dataset or uplod file, and a data frame)
st.sidebar.header("Configuration 📁")

sample_data = st.sidebar.checkbox("Use Sample Dataset")

upload_file = st.sidebar.file_uploader("Upload your CSV dataset", type=["csv"])

@st.cache_data
def load_sample_data():
    from sklearn.datasets import load_iris
    data = load_iris(as_frame=True)
    return data.frame

if sample_data:
    df = load_sample_data()
elif upload_file is not None:
    try:
        df = pd.read_csv(upload_file)
    except Exception as e:
        st.error(f"Error reading the CSV file: {e}")
        st.stop()
else:
    st.warning("Please upload a CSV file or use the sample dataset.")
    st.stop()

# User is able preview the dataset
st.subheader("Dataset Preview 🔍")
st.dataframe(df.head())

# User is prompted to select features and target 
target = st.selectbox("Select the target variable 🎯", df.columns)
features = st.multiselect("Select feature columns 🧰", [col for col in df.columns if col != target])
if not features:
    st.error("Select at least one feature.")
    st.stop()

# The configuration of the train/test split
st.sidebar.subheader("Train/Test Split 🧪")
test_size = st.sidebar.slider("Test set proportion", 0.1, 0.5, 0.2)

# User is prompted to select a model, either decision or logistic regression. Considering the nature of most datasets, I thought it made sense to choose log reg as the default setup for the app
st.sidebar.subheader("Model Selection 📊")
model_option = st.sidebar.selectbox("Choose a model", ["Decision Tree", "Logistic Regression"])
if model_option == "Decision Tree":
    max_depth = st.sidebar.slider("Decision Tree: Maximum Depth", 1, 20, 5)
else:
    st.sidebar.info("Using default Logistic Regression parameters")

# Model training. As most apps evaluated in class did not explain why certain features did not work well given the nature of the dataset provided by the user, I thought it made sense to include some kind of specification/error message here to ensure better UX. I also split, train, and evluate the model here, while sharing some output results.
if st.button("Train Model 🚀"):
    X = df[features]
    y = df[target]

    if model_option in ["Decision Tree", "Logistic Regression"]:
        target_type = type_of_target(y)
        if target_type not in ["binary", "multiclass"]:
            st.error("❗ For classification, choose a categorical target (e.g., species/class labels).")
            st.stop()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    if model_option == "Decision Tree":
        model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    else:
        model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)
    cr = classification_report(y_test, predictions)

    st.subheader("Model Performance ✅")
    st.write(f"**Accuracy:** {round(acc, 4)}")
    st.text("Classification Report:\n" + cr)

    # I thought it was valuable to add some visualizations here. In light of what we've been discussing in class over the last few weeks, I thought it was good to have a Confusion Matrix and Feature Importance to begin with
    fig, ax = plt.subplots()
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(ax=ax, cmap="Blues", colorbar=False)
    ax.set_title("Confusion Matrix", fontsize=14, fontweight='bold')
    st.pyplot(fig)

    if model_option == "Decision Tree":
        st.subheader("Feature Importance (Decision Tree) 🌲")

        importances = model.feature_importances_
        importance_df = pd.DataFrame({
            'Feature': features,
            'Importance': importances
        }).sort_values(by='Importance', ascending=False)

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(data=importance_df, x='Importance', y='Feature', ax=ax)
        ax.set_title("Decision Tree Feature Importance", fontsize=14, fontweight='bold')
        ax.set_xlabel("Importance", fontsize=12)
        ax.set_ylabel("Feature", fontsize=12)
        st.pyplot(fig)

# Beyond the visualizations described and coded previously, I thought it would be useful to have a Correlation Heatmap and Histogram + Kernel Density Estimation of a feature. I'll be providing more extensive rationales of why I chose these visualizations in the ReadMe 
st.subheader("Feature Correlation Heatmap 🔗")
with st.expander("See correlation between selected numeric features 🔍"):
    numeric_cols = df[features + [target]].select_dtypes(include='number')
    if not numeric_cols.empty:
        corr = numeric_cols.corr()
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
        ax.set_title("Correlation Matrix", fontsize=14, fontweight='bold')
        st.pyplot(fig)
    else:
        st.info("No numeric columns found to plot correlation matrix.")

st.subheader("Histogram + KDE of a Feature 📊")
selected_hist_feature = st.selectbox("Choose a feature to explore distribution 📈", features)
if selected_hist_feature:
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df[selected_hist_feature], kde=True, color="skyblue", edgecolor="black", ax=ax)
    ax.set_title(f"Distribution of {selected_hist_feature}", fontsize=14, fontweight='bold')
    ax.set_xlabel(selected_hist_feature, fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    st.pyplot(fig)