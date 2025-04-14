import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

# Title and introduction
st.title("Interactive Supervised Machine Learning App")
st.write("""
This app allows you to upload your dataset, select features, pick a target variable,
choose a machine learning model (Decision Tree or Logistic Regression), adjust key hyperparameters, 
and see model performance metrics.
""")

# Sidebar configuration
st.sidebar.header("Configuration")

# Option to use sample dataset
sample_data = st.sidebar.checkbox("Use Sample Dataset")

# Option to upload your CSV file
upload_file = st.sidebar.file_uploader("Upload your CSV dataset", type=["csv"])

# Function to load sample dataset
@st.cache_data
def load_sample_data():
    from sklearn.datasets import load_iris
    data = load_iris(as_frame=True)
    return data.frame

# Define DataFrame based on user input
if sample_data:
    df = load_sample_data()
elif upload_file is not None:
    try:
        df = pd.read_csv(upload_file)
    except Exception as e:
        st.error(f"Error reading the CSV file: {e}")
        st.stop()
else:
    st.warning("Awaiting CSV file upload or enabling the sample dataset.")
    st.stop()

# Display dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# User selects the target variable and features
target = st.selectbox("Select the target variable", df.columns)
features = st.multiselect("Select feature columns (at least one)", [col for col in df.columns if col != target])
if not features:
    st.error("Please select at least one feature to continue.")
    st.stop()

# Sidebar options for train/test split
st.sidebar.subheader("Train/Test Split")
test_size = st.sidebar.slider("Test set proportion", min_value=0.1, max_value=0.5, value=0.2)

# Sidebar options for model selection
st.sidebar.subheader("Model Selection")
model_option = st.sidebar.selectbox("Choose a model", ["Decision Tree", "Logistic Regression"])

# Model-specific hyperparameters
if model_option == "Decision Tree":
    max_depth = st.sidebar.slider("Decision Tree: Maximum Depth", min_value=1, max_value=20, value=5)
else:
    # For Logistic Regression, you could add other hyperparameters such as the regularization parameter.
    st.sidebar.info("Default hyperparameters will be used for Logistic Regression.")

if st.button("Train Model"):
    # Prepare data for training
    X = df[features]
    y = df[target]
    
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    # Initialize and train the selected model
    if model_option == "Decision Tree":
        model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    else:
        model = LogisticRegression(max_iter=1000)
    
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    
    # Compute performance metrics
    acc = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)
    cr = classification_report(y_test, predictions)
    
    # Display performance results
    st.subheader("Model Performance")
    st.write("**Accuracy:**", round(acc, 4))
    st.write("**Confusion Matrix:**")
    st.write(cm)
    st.text("**Classification Report:**\n" + cr)