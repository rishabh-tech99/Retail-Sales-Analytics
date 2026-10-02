# Retail Sales Analytics & Profit Prediction

An end-to-end **Data Analytics + Machine Learning** project designed to analyze retail sales performance, identify profit patterns, forecast future sales, and predict order profitability.

##  Project Overview

This project analyzes **3,000 retail orders from 2023–2025** and provides insights into sales, profit, discounts, products, categories, regions, and customer segments.

The project combines:

* Data cleaning and feature engineering
* Exploratory Data Analysis (EDA)
* Sales and profit analysis
* Machine Learning for profit prediction
* Sales forecasting
* Flask REST APIs
* Interactive HTML + Chart.js dashboard

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**
* **Flask**
* **HTML/CSS**
* **Chart.js**
* **Jupyter/VS Code**

##  Dataset

Dataset: `data/retail_sales.csv`

The dataset contains **3,000 orders** covering the period **2023–2025**.

### Main Columns

| Column       | Description             |
| ------------ | ----------------------- |
| `order_id`   | Unique order identifier |
| `order_date` | Date of order           |
| `region`     | Sales region            |
| `segment`    | Customer segment        |
| `category`   | Product category        |
| `product`    | Product name            |
| `quantity`   | Quantity ordered        |
| `unit_price` | Price per unit          |
| `discount`   | Discount applied        |
| `sales`      | Total sales amount      |
| `profit`     | Order profit            |

The dataset is generated reproducibly using `generate_data.py`.

The project can also be adapted to the **Kaggle Superstore dataset** by maintaining the required column names.

## Project Pipeline

```text
Data Collection / Generation
            ↓
Data Cleaning & Feature Engineering
            ↓
Exploratory Data Analysis
            ↓
Sales & Profit Analysis
            ↓
Profit Prediction
            ↓
Sales Forecasting
            ↓
Flask REST API
            ↓
Interactive Dashboard
```

##  Exploratory Data Analysis

The EDA focuses on:

* Overall sales and profit KPIs
* Year-over-year sales trends
* Monthly sales patterns
* Category performance
* Regional performance
* Product-level performance
* Discount vs. profit relationship
* Quantity and sales analysis
* Segment-wise performance

##  Machine Learning

### 1. Profit Prediction

A **Random Forest Regressor** is used to estimate order-level profit.

The model is evaluated using:

* R² Score
* Mean Absolute Error (MAE)

A 20% test split is used for model evaluation.

### 2. Sales Forecasting

A **Linear Regression** model with trend and seasonal features is used to forecast sales for the next **6 months**.

The forecasting pipeline considers:

* Time trend
* Monthly seasonality
* Historical sales patterns

##  Key Insights

The analysis highlights several important patterns:

* Sales show year-over-year growth.
* Sales generally peak during **November and December**.
* **Technology** generates the highest sales among the major categories.
* **Office Supplies** shows stronger profit margins.
* **Furniture** has comparatively lower margins.
* Higher discounts are associated with lower average profit.
* For some low-margin products, discounts above approximately **20–30%** can result in negative profitability.

> These insights are based on the generated dataset and may change when a different dataset is used.

##  Deployment

The project uses **Flask** to provide REST APIs and serve an interactive web dashboard.

The dashboard uses **Chart.js** to visualize:

* Sales trends
* Profit trends
* Category performance
* Regional performance
* Forecasted sales
* Profit prediction results

##  Project Structure

```text
retail-sales-analytics-profit-prediction/
│
├── app.py
├── generate_data.py
├── requirements.txt
│
├── data/
│   └── retail_sales.csv
│
├── templates/
│   └── index.html
│
└── README.md
```

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rishabh-tech99/retail-sales-analytics-profit-prediction.git
cd retail-sales-analytics-profit-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the dataset

```bash
python generate_data.py
```

### 4. Start the Flask application

```bash
python app.py
```

### 5. Open the dashboard

```text
http://127.0.0.1:5000
```

## Future Scope

* Customer segmentation using **K-Means Clustering**
* SQLite/MySQL database integration
* User CSV upload functionality
* Automated model retraining
* Advanced forecasting models
* Cloud deployment
* Authentication and user management
* Advanced Power BI integration



---

⭐ If you find this project useful, consider giving the repository a star.
