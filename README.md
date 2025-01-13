# Ecommerce Linear Regression Project 

This is a learning project that involves building and evaluating a linear regression model to analyze customer data from an ecommerce website. The model predicts the yearly amount spent by a customer based on several factors like session length, time spent on the app, time on the website, and membership duration.

## Table of Contents
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Structure](#code-structure)
5. [Outputs](#outputs)
6. [Summary](#summary)
7. [Requirements](#requirements)
8. [Acknowledgements](#acknowledgements)

## Project Description
The following dataset information was used to predict the yearly amount spent by a customer: 
- **Avg. Session Length**: Average session duration in minutes.
- **Time on App**: Time spent on the mobile application.
- **Time on Website**: Time spent on the website.
- **Length of Membership**: Membership duration in years.
- **Yearly Amount Spent**: Total yearly expenditure of the customer.

The goal of the project is to:
1. Explore and visualize the information provided in the dataset.
2. Train a linear regression model to predict the yearly amount spent.
3. Evaluate the linear regression model's performance.

## Installation
1. Clone the repository or download the script.
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Place the `ecommerce_customers.csv` file in the same directory as the script.

## Usage
1. Run the script using Python:
   ```bash
   python linear_regression.py
   ```
2. The script performs the following:
   - Loads the dataset.
   - Performs exploratory data analysis (EDA).
   - Splits the data into training and testing sets.
   - Trains a linear regression model.
   - Evaluates the model with metrics and visualizations.

## Code Structure
The code is organized into modular functions:

- **`load_data(file_path)`**: Loads the dataset from a CSV file.
- **`explore_data(data)`**: Explores the dataset with visualizations and summaries.
- **`split_data(data)`**: Splits the data into training and testing sets.
- **`train_model(X_train, y_train)`**: Trains a linear regression model.
- **`evaluate_coefficients(model, feature_columns)`**: Prints the model coefficients for interpretation.
- **`predict_and_evaluate(model, X_test, y_test)`**: Predicts test data and evaluates model performance.

## Outputs
1. **Visualizations**:
   - Joint plots: Relationships between variables.
     
     ![jointplot_II](https://github.com/user-attachments/assets/da2523f4-b460-46fc-add9-ac9e6afeab6b)
     
   - Pair plot: Overall relationships among features.
     
     ![pairplot](https://github.com/user-attachments/assets/794a39e0-2d30-4ad6-9833-585ffe1b9469)

   - Linear model plot,regression line for significant variables.
        
     ![lmplot](https://github.com/user-attachments/assets/f93695f7-886f-4a2a-bd31-40343129aa63)
     
     
   - Residual distribution plot: Error analysis.
     
     ![displot](https://github.com/user-attachments/assets/a3fc2dcf-4874-4535-9dd5-f26346afc31b)

2. **Metrics**:
   - Mean Absolute Error (MAE)
   - Mean Squared Error (MSE)
   - Root Mean Squared Error (RMSE)

3. **Coefficients Table**: Indicates the contribution of each feature to the target variable.

## Summary

## Requirements
- Python 3.6+
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

## Acknowledgements
Dataset: The `ecommerce_customers.csv` file used for analysis.

Resource: Alejandro AO project walkthrough (https://www.youtube.com/watch?v=My4JgIeFdWk&ab_channel=AlejandroAO-Software%26Ai).
