# Codex Beverage Price Prediction

This project aims to predict the **price range of beverages** for customers based on various demographic and behavioral features such as income, age, drinking time, and flavor preferences. It leverages multiple machine learning models and uses **MLflow** for experiment tracking and comparison.

## 🧠 Problem Statement

The goal is to help beverage companies or vendors determine the appropriate **price segment** for different customer profiles, aiding in **personalized pricing strategies**.

## 📦 Dataset Features

The dataset includes features like:

- Age
- Income
- Preferred beverage flavor
- Previous purchase frequency
- Other customer demographic and behavioral data

## 🔧 Tasks Performed

- ✅ **Data Cleaning**  
- ✅ **Feature Engineering**
- ✅ **Model Training**
- ✅ **Model Evaluation** using MLflow
- ✅ **Model Comparison**

## 🤖 Machine Learning Models Used

The following classification models were trained and evaluated:

1. Gaussian Naive Bayes
2. Logistic Regression
3. Support Vector Machine (SVM)
4. Random Forest
5. XGBoost
6. Light Gradient Boosting Machine (LightGBM)

## 🏆 Best Performing Model

- **XGBoost** and **Light GBM** achieved the best performance in terms of accuracy and generalization on the test data.

## 📊 Evaluation Metrics

| Model                  | Accuracy | Precision | Recall | F1 Score | CV Score |
|------------------------|----------|-----------|--------|----------|----------|
| Gaussian Naive Bayes   | 0.5644   | 0.5718    | 0.5644 | 0.5271   | 0.5599   |
| Logistic Regression    | 0.8452   | 0.8459    | 0.8452 | 0.8454   | 0.8455   |
| SVM                    | 0.8723   | 0.8725    | 0.8723 | 0.8724   | 0.8667   |
| Random Forest          | 0.8822   | 0.8835    | 0.8822 | 0.8825   | 0.8800   |
| **XGBoost**            | **0.9200**   | **0.9203**    | **0.9200** | **0.9201**   | **0.9190**   |
| **LightGBM**               | **0.9226** | **0.9227** | **0.9226** | **0.9226** | **0.9218** |


## 🛠 Tools & Technologies

- Python
- scikit-learn
- XGBoost
- LightGBM
- MLflow
- pandas, NumPy, matplotlib, seaborn

## 📈 MLflow Tracking

All experiments were logged and compared using **MLflow**, allowing for easy reproducibility and tracking of:

- Parameters
- Metrics
- Models
- Artifacts

Link: [Dagshub](https://dagshub.com/2411chirag/Codex-Price-Pred/experiments)


