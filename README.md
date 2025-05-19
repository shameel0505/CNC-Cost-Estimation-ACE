# CNC Cost Estimation Project

## Objective

Develop a machine learning model to predict CNC machining cost or cycle time using a dataset of CNC-machined parts. The project includes data cleaning, feature engineering, model training, visualization, and interpretation.

---

## Project Tasks

### 1. Data Gathering
- Collected a dataset with relevant CNC machining features such as material type, part dimensions, cycle times, and estimated costs.
- Data sources included CNC machining forums, manufacturing listings, and publicly available engineering repositories.
- Followed ethical scraping practices and avoided login-gated or restricted sites.

### 2. Data Understanding & Cleaning
- Loaded and explored the dataset to understand the features and data quality.
- Handled missing values, duplicates, and corrected data types.
- Visualized data distributions and patterns to guide cleaning.

### 3. Feature Engineering
- Created new features such as cost per unit volume and complexity indices.
- Explained the rationale behind each feature with respect to machining processes.
- Analyzed how these features potentially impact machining cost.

### 4. Visualization & Model Training
- Visualized relationships between cost/cycle time and variables like material, volume, and feature count using matplotlib and seaborn.
- Trained regression models (Linear Regression and Random Forest) to predict quoted cost or cycle time.
- Evaluated model performance using MAE, RMSE, and visualized predicted vs. actual values.
- Interpreted feature importance to understand key cost drivers.

### 5. Final Analysis & Reflection
- Summarized what worked well in modeling and challenges faced.
- Suggested improvements leveraging additional data or domain expertise.
- Reflected on manufacturing data characteristics and feature relevance.

---

## How to Run

1. Clone this repository.
2. Set up a Python virtual environment.
3. Install required packages listed in `requirements.txt`.
4. Run the Jupyter notebook `CNC_Cost_Estimation.ipynb` sequentially to reproduce analysis and results.

---

## Tools Used

- Python (NumPy, pandas, scikit-learn, matplotlib, seaborn)
- Jupyter Notebook
- Web scraping tools (BeautifulSoup, Selenium) for data gathering

---

## Summary

This project demonstrates the application of core data science skills to manufacturing data. The trained models provide insights into the factors influencing CNC machining costs and cycle times, supporting better cost estimation and production planning.

---

Feel free to reach out for any questions or clarifications.
