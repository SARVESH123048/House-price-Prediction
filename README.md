# 🏠 House Price Prediction

This repository contains a machine learning project focused on predicting house prices using various regression techniques. The dataset used is sourced from the **Kaggle House Prices - Advanced Regression Techniques** competition.

## 📁 Files

- `House price Prediction.ipynb`: Main Jupyter Notebook containing the entire pipeline including:
  - Data loading and preprocessing
  - Exploratory data analysis (EDA)
  - Feature engineering
  - Outlier detection
  - Model training (Logistic Regression, Decision Tree, SVM)
  - Evaluation using Accuracy, F1 Score, and Residual Analysis
  - Error and Outlier Visualization

## 📊 Dataset

- Dataset Source: [Kaggle House Price Prediction](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
- Files used: `train.csv` and optionally `test.csv`
- Target Variable: `SalePrice`
- Features: 79 variables related to residential homes in Ames, Iowa

## ⚙️ Technologies Used

- Python
- NumPy, Pandas
- Matplotlib, Seaborn
- Scikit-learn

## 📌 Project Highlights

- ✅ Data Cleaning and Null Handling
- ✅ Removal of High-NA Columns and Rows
- ✅ Outlier Detection with Boxplots
- ✅ Feature Scaling using StandardScaler
- ✅ Classification of Price Quality into Levels
- ✅ Multi-algorithm training and evaluation
- ✅ Error and residual visualization

## 🧠 Models Used

- Logistic Regression
- Decision Tree Classifier
- Support Vector Machine (SVM)

## 📈 Evaluation Metrics

- Accuracy Score
- F1 Score
- Residual Plots
- Error Analysis
- Outlier vs Error Comparison Graphs

## 🚀 Getting Started

### Prerequisites

Install the dependencies:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
