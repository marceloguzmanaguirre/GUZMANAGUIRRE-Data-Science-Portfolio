import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.utils.multiclass import type_of_target
from sklearn.preprocessing import LabelEncoder

# Header and a brief description of what the user should do (upload data, choose features, etc.)
st.title("Interactive Supervised Machine Learning App 🧠")
st.write("""
Upload a dataset (or use the sample), choose features and a target, train a model, and explore results visually!
""")

# Sidebar (inludes option for user to use sample dataset or uplod file, and a data frame)
st.sidebar.header("Configuration 📁")

sample_data = st.sidebar.radio("Select Data Source", ["Use Sample Dataset", "Upload CSV File"])

# Here, the @st.cache_data decorator efficiently caches the Iris dataset to improve app performance by loading it only once. The load_sample_data() function imports the classic Iris flower dataset from scikit-learn, converts it to a pandas DataFrame format, and returns it for use in the Streamlit app
@st.cache_data
def load_sample_data():
    from sklearn.datasets import load_iris
    data = load_iris(as_frame=True)
    return data.frame

df = None

# This code handles data loading based on user choice: if the user selects "Use Sample Dataset," it loads the cached Iris dataset; otherwise, it prompts the user to upload a CSV file, loads it if provided, and displays appropriate success/error messages. If no data source is available, it warns the user and stops execution
if sample_data == "Use Sample Dataset":
    df = load_sample_data()
elif sample_data is not None:
    uploaded_file = st.sidebar.file_uploader("Upload your CSV", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success("File uploaded successfull")
        except Exception as e:
            st.sidebar.error(f"Error reading file")
            st.stop()
    else:
        st.sidebar.warning("Upload a file to continue")
else:
    st.warning("Please upload a CSV file or use the sample dataset.")
    st.stop()

# Bugfix: preventing code from executinf if df is none
if df is None:
    st.warning("Please upload a CSV file or use the sample dataset")
    st.stop()

# Encoding categorical features and handling missing values
df.dropna(inplace=True)

for col in df.select_dtypes(include="object").columns:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

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
test_size = st.sidebar.slider("This slider sets the ratio of training to testing data. More training data can improve learning, while testing data checks model performance", 0.1, 0.5, 0.2)

# This code adds a model selection interface in the sidebar. It displays a dropdown menu allowing users to choose between "Decision Tree" and "Logistic Regression" models, then conditionally presents appropriate hyperparameter controls - a slider for tree depth (1-20, default 5) if Decision Tree is selected, or a slider for maximum iterations (2-1000, default 100) if Logistic Regression is chosen, providing intuitive model customization options
st.sidebar.subheader("Model Selection 📊")
model_option = st.sidebar.selectbox("Choose a model", ["Decision Tree", "Logistic Regression"])
if model_option == "Decision Tree":
    max_depth = st.sidebar.slider("Decision Tree: Maximum Depth - controls model complexity", 1, 20, 5)
elif model_option == "Logistic Regression":
    max_iter = st.sidebar.slider("Select max_iter - how many times the model can update during training", 2, 1000, 100)


# When the user clicks the "Train Model" button, this code splits the data into features and target, validates that the target is suitable for classification, divides data into training and testing sets, then trains either a Decision Tree or Logistic Regression model based on user selection. After training, it evaluates model performance using accuracy scores and classification reports, and visualizes results through a confusion matrix and, for Decision Trees, a feature importance chart
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
        model = LogisticRegression(max_iter=max_iter)

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)
    cr = classification_report(y_test, predictions, zero_division=0)

    st.subheader("Model Performance ✅")
    st.write(f"**Accuracy:** {round(acc, 4)}")
    st.text("Classification Report:\n" + cr)

    # Here, I create and display a confusion matrix visualization. It first sets up a matplotlib figure and axis, then uses ConfusionMatrixDisplay to plot the confusion matrix (stored in variable "cm") with class labels from the model. The visualization uses a blue color scheme ("Blues"), removes the colorbar for cleaner appearance, adds a bold title, and displays the resulting figure in the Streamlit app using st.pyplot()
    fig, ax = plt.subplots()
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(ax=ax, cmap="Blues", colorbar=False)
    ax.set_title("Confusion Matrix", fontsize=14, fontweight='bold')
    st.pyplot(fig)
    
    # This conditionally displays feature importance for Decision Tree models. It extracts feature importance values from the model, creates a DataFrame pairing feature names with their importance scores, sorts them by importance in descending order, and generates a horizontal bar chart using seaborn
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

# This code creates an expandable section displaying a correlation heatmap, filtering for numeric columns among the selected features and target, calculates correlations between these variables, and visualizes them as a heatmap using seaborn with a coolwarm color scheme and numerical annotations. Essentially, visualization helps users identify relationships between features, showing which variables are positively or negatively correlated, or displaying an informational message if no numeric columns are available
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

# Interactive feature distribution visualization is created here, adding a dropdown menu allowing users to select any feature for analysis, then generates a histogram with an overlaid kernel density estimate (KDE) curve using seaborn
st.subheader("Histogram + KDE of a Feature 📊")
selected_hist_feature = st.selectbox("Choose a feature to explore distribution 📈", features)
if selected_hist_feature:
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df[selected_hist_feature], kde=True, color="skyblue", edgecolor="black", ax=ax)
    ax.set_title(f"Distribution of {selected_hist_feature}", fontsize=14, fontweight='bold')
    ax.set_xlabel(selected_hist_feature, fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    st.pyplot(fig)