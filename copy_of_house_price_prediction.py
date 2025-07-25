# -*- coding: utf-8 -*-
"""Copy of House price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ceQdv6YFAEE22SpZibLHHdxxksmrjzcM
"""

!pip install kaggle==1.5.12

!mkdir -p ~/.kaggle

!cp kaggle-2.json ~/.kaggle/

!chmod 600 ~/.kaggle/kaggle-2.json

import pandas as pd

df = pd.read_csv('Mumbai.csv')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error

df = pd.read_csv('Mumbai.csv')
df.head()
df.info()
df.describe()

null_counts = df.isnull().sum()
null_percentages = (null_counts / len(df)) * 100
null_info = pd.DataFrame({'Null Count': null_counts, 'Null Percentage': null_percentages})
print(null_info)

threshold = 50  # Example threshold
cols_to_drop = null_info[null_info['Null Percentage'] > threshold].index
df.drop(columns=cols_to_drop, inplace=True)

threshold_rows = 5  # Example threshold for number of missing values per row
df.dropna(thresh=len(df.columns) - threshold_rows, inplace=True)

print(df.columns)

# Try accessing a column to see if it exists with the exact name
try:
    print(df['ID'].head())
except KeyError:
    print("Column 'ID' not found.")

try:
    print(df['Notes'].head())
except KeyError:
    print("Column 'Notes' not found.")

# Assuming 'Price' is your target column. Replace with the actual target column name.
if 'Price' in df.columns:
    X = df.drop('Price', axis=1)  # Features are all columns except the target
    y = df['Price']            # Target variable
else:
    print("Error: 'Price' column not found. Please define your target column.")

# Now you can proceed with one-hot encoding on X
X = pd.get_dummies(X, drop_first=True)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check if the columns exist before plotting
if 'ActualCategoricalColumnName' in df.columns and 'ActualNumericalColumnName' in df.columns:
    sns.boxplot(x='ActualCategoricalColumnName', y='ActualNumericalColumnName', data=df)
    plt.xticks(rotation=90)
    plt.show()
else:
    print("Error: One or both specified columns for the boxplot were not found in the DataFrame.")

# Print columns after cleaning to verify
print(df.columns)

# Try accessing 'sector' and 'price' to see if they exist with the exact names
try:
    print(df['sector'].head())
except KeyError:
    print("Column 'sector' not found. Please check the column name.")

try:
    print(df['price'].head())
except KeyError:
    print("Column 'price' not found. Please check the column name.")


def classify_price_quality(row):
    # Ensure 'sector' and 'price' columns exist in the row
    if 'sector' not in row or 'price' not in row:

        return None # Or a placeholder like 'Unknown'

    sector = row['sector']
    price = row['price']


    sector_prices = df[df['sector'] == sector]['price']

    # Handle cases where sector_prices might be empty or have too few values
    if sector_prices.empty or len(sector_prices) < 4:
         return 'Cannot Classify' # Or handle appropriately

    q1 = sector_prices.quantile(0.25)
    q2 = sector_prices.quantile(0.5)
    q3 = sector_prices.quantile(0.75)

    if price <= q1:
        return 'Low'
    elif price <= q2:
        return 'Medium-Low'
    elif price <= q3:
        return 'Medium-High'
    else:
        return 'High'


if 'sector' in df.columns and 'price' in df.columns:
    df['price_quality'] = df.apply(classify_price_quality, axis=1)
else:
    print("Cannot apply price quality classification: 'sector' or 'price' column not found.")

# file ipython-input-19-67c97480b203
# Assuming 'Price' is your target column. Replace with the actual target column name if different.
if 'Price' in df.columns:
    X = df.drop('Price', axis=1)  # Features are all columns except the target
    y = df['Price']            # Target variable
else:
    # This message indicates the expected target column 'Price' was not found.
    # You need to inspect df.columns to find the correct target column name.
    print("Error: 'Price' column not found. Please define your target column.")
    # You might want to stop execution or handle this case more robustly
    # to prevent subsequent errors. For now, we assume 'Price' exists based on the error.

# Now you can proceed with one-hot encoding on X
X = pd.get_dummies(X, drop_first=True)

# file ipython-input-28-67c97480b203
# Print columns after cleaning to verify
print(df.columns)

# Try accessing 'sector' and the *correct* price column name (assuming 'Price')
try:
    print(df['sector'].head())
except KeyError:
    print("Column 'sector' not found. Please check the column name.")

try:
    # Use the actual price column name, which is likely 'Price' based on earlier code
    print(df['Price'].head())
except KeyError:
    # This error means the 'Price' column isn't in the dataframe after cleaning.
    # Review previous cleaning steps that might have removed it unintentionally.
    print("Column 'Price' not found. Please check the column name.")



def classify_price_quality(row):
    # Ensure 'sector' and the *correct* price column name ('Price') exist in the row
    # Use the actual price column name
    price_column_name = 'Price'

    if 'sector' not in row or price_column_name not in row:
        # You might want to handle this case, perhaps return a default value
        # or skip this row depending on your needs.
        return None # Or a placeholder like 'Unknown'

    sector = row['sector']
    price = row[price_column_name] # Use the actual price column name


    sector_prices = df[df['sector'] == sector][price_column_name]

    # Handle cases where sector_prices might be empty or have too few values
    # A quartile calculation requires at least 4 values.
    if sector_prices.empty or len(sector_prices) < 4:
         return 'Cannot Classify' # Or handle appropriately

    # Calculate quartiles using the actual price column name
    q1 = sector_prices.quantile(0.25)
    q2 = sector_prices.quantile(0.5)
    q3 = sector_prices.quantile(0.75)

    if price <= q1:
        return 'Low'
    elif price <= q2:
        return 'Medium-Low'
    elif price <= q3:
        return 'Medium-High'
    else:
        return 'High'


price_column_name = 'Price'
if 'sector' in df.columns and price_column_name in df.columns:
    df['price_quality'] = df.apply(classify_price_quality, axis=1)
    print("'price_quality' column created successfully.")
else:

    print(f"Cannot apply price quality classification: 'sector' or '{price_column_name}' column not found.")

if 'price_quality' not in df.columns:
    print("Error: 'price_quality' column not found. It was likely not created in the previous step.")

# Use the correct price column name ('Price') and 'price_quality' if it exists
columns_to_drop = ['price_quality']
# Assuming your actual numerical target column is 'Price'
price_column_name = 'Price'
if price_column_name in df.columns:
    columns_to_drop.append(price_column_name)
else:

    print(f"Warning: Original target column '{price_column_name}' not found in df.")
    # If 'Price' was the original target and is missing, X and y might be empty or incorrect.


# Ensure the columns we intend to drop actually exist in df
existing_cols_to_drop = [col for col in columns_to_drop if col in df.columns]

if existing_cols_to_drop:
    X = df.drop(existing_cols_to_drop, axis=1)  # Features
else:
    # If neither 'Price' nor 'price_quality' exist, dropping them will fail.
    # This suggests a major issue with previous steps.
    print("Error: Neither original target column nor 'price_quality' found to drop.")

    X = df.copy() # Or assign None, depending on desired behavior


# Ensure 'price_quality' was created before using it as the target
if 'price_quality' in df.columns:
    y = df['price_quality']  # Target
else:
    print("Error: Cannot assign target variable y. 'price_quality' column not found.")
    # Handle this case, e.g., assign y = None or stop execution.
    y = None # Assign None to y


# Proceed only if X and y are valid
if X is not None and y is not None and not X.empty and not y.empty:
    # One-hot encode categorical features in X
    X = pd.get_dummies(X, drop_first=True)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train models
    # Logistic Regression
    lr_model = LogisticRegression(max_iter=1000) # Added max_iter for potential convergence issues
    lr_model.fit(X_train, y_train)

    # Decision Tree
    dt_model = DecisionTreeClassifier()
    dt_model.fit(X_train, y_train)

    # SVM
    svm_model = SVC()
    svm_model.fit(X_train, y_train)

    print("Models trained successfully.")
else:
    print("Skipping model training due to errors in data preparation.")

print("Columns in df before creating price_quality:")
print(df.columns)


price_column_name = 'Price'

# Try accessing 'sector' and the *correct* price column name ('Price')
try:
    print(f"\nFirst 5 rows of '{price_column_name}':")
    print(df[price_column_name].head())
except KeyError:
    print(f"Column '{price_column_name}' not found. Please check the column name.")

try:
    print("\nFirst 5 rows of 'sector':")
    print(df['sector'].head())
except KeyError:
    print("Column 'sector' not found. Please check the column name.")



def classify_price_quality(row):
    # Use the actual price column name
    price_column_name_in_row = 'Price' # Use the consistent name here too

    # Ensure 'sector' and the *correct* price column name exist in the row
    if 'sector' not in row or price_column_name_in_row not in row:

        return None # Or a placeholder like 'Unknown'

    sector = row['sector']
    price = row[price_column_name_in_row] # Use the actual price column name


    if price_column_name_in_row not in df.columns or 'sector' not in df.columns:
         # This case should ideally be caught by the outer check, but adding defensively
         return 'Cannot Classify'

    sector_prices = df[df['sector'] == sector][price_column_name_in_row]


    if sector_prices.empty or len(sector_prices) < 4:
         return 'Cannot Classify' # Or handle appropriately

    # Calculate quartiles using the actual price column name
    q1 = sector_prices.quantile(0.25)
    q2 = sector_prices.quantile(0.5)
    q3 = sector_prices.quantile(0.75)

    if price <= q1:
        return 'Low'
    elif price <= q2:
        return 'Medium-Low'
    elif price <= q3:
        return 'Medium-High'
    else:
        return 'High'


price_column_name_for_apply = 'Price' # Use the consistent name here too
if 'sector' in df.columns and price_column_name_for_apply in df.columns:
    # Add a check for NaN/None values in the relevant columns before applying
    if not df[['sector', price_column_name_for_apply]].isnull().any().any():
        df['price_quality'] = df.apply(classify_price_quality, axis=1)
        print("'price_quality' column created successfully.")
    else:
        print(f"Cannot apply price quality classification: Found missing values in 'sector' or '{price_column_name_for_apply}'.")
        # You might want to drop rows with NaNs in these columns before applying
else:

    print(f"Cannot apply price quality classification: 'sector' or '{price_column_name_for_apply}' column not found.")


# Print columns again to confirm if price_quality was added
print("\nColumns in df after attempting to create price_quality:")
print(df.columns)

print("Columns in df before data preparation for modeling:")
print(df.columns)


classification_target_column = 'price_quality'

original_price_column = 'Price'



if classification_target_column not in df.columns:
    print(f"Error: Classification target column '{classification_target_column}' not found. Model training skipped.")

    X = None
    y = None
else:

    columns_to_drop = [classification_target_column]

    if original_price_column in df.columns:
        columns_to_drop.append(original_price_column)
    else:
        print(f"Warning: Original numerical price column '{original_price_column}' not found to drop from features.")


    existing_cols_to_drop = [col for col in columns_to_drop if col in df.columns]

    if existing_cols_to_drop:
        X = df.drop(columns=existing_cols_to_drop)  # Features
        print(f"\nSuccessfully dropped columns: {existing_cols_to_drop} from features (X).")
    else:

        print("Error: Neither classification target nor original price column found to drop. X will be a copy of df.")
        X = df.copy()


    y = df[classification_target_column]
    print(f"Successfully assigned target variable y as '{classification_target_column}'.")

if X is not None and y is not None and not X.empty and not y.empty:
    print(f"\nX shape before one-hot encoding: {X.shape}")
    print(f"y shape: {y.shape}")


    try:
        X = pd.get_dummies(X, drop_first=True)
        print(f"X shape after one-hot encoding: {X.shape}")
    except Exception as e:
        print(f"Error during one-hot encoding: {e}")
        X = None # Invalidate X if get_dummies fails


    if X is not None and not X.empty:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("\nData split into training and testing sets.")
        print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
        print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")


        # Train models
        print("\nTraining models...")
        try:
            # Logistic Regression

            lr_model = LogisticRegression(max_iter=1000, solver='liblinear') # Changed solver for potentially faster convergence on smaller datasets
            lr_model.fit(X_train, y_train)
            print("Logistic Regression model trained.")

            # Decision Tree
            dt_model = DecisionTreeClassifier(random_state=42)
            dt_model.fit(X_train, y_train)
            print("Decision Tree model trained.")


            svm_model = SVC(random_state=42)
            svm_model.fit(X_train, y_train)
            print("SVM model trained.")

            print("\nModels trained successfully.")

        except Exception as e:
            print(f"An error occurred during model training: {e}")

            lr_model = None
            dt_model = None
            svm_model = None
            print("Model training failed due to an error.")

    else:
        print("Skipping model training because X is invalid or empty after one-hot encoding.")

        lr_model = None
        dt_model = None
        svm_model = None


else:
    print("Skipping model training due to errors in data preparation (X or y is None/empty).")

    lr_model = None
    dt_model = None
    svm_model = None

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


if 'dt_model' in locals() and dt_model is not None and 'X_test' in locals() and X_test is not None and not X_test.empty:
    dt_pred = dt_model.predict(X_test)


    if 'y_test' in locals() and y_test is not None and not y_test.empty:
        cm = confusion_matrix(y_test, dt_pred, labels=dt_model.classes_)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=dt_model.classes_)
        disp.plot()
        plt.show()
    else:
        print("Error: y_test is not defined or is empty. Cannot compute confusion matrix.")
else:
    print("Error: dt_model or X_test is not defined or is empty. Cannot make predictions.")