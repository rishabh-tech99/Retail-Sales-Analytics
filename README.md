# Retail Sales Analytics & Profit Prediction

**Problem:** A retailer wants to understand sales/profit patterns, forecast demand and estimate order profitability.
**Dataset:** `data/retail_sales.csv` – 3,000 orders (2023-2025), columns: order_id, order_date, region, segment, category, product, quantity, unit_price, discount, sales, profit. Generated reproducibly by `generate_data.py` (you can swap in the Kaggle "Superstore" dataset by keeping the same column names).

## Pipeline
1. Data collection/generation → 2. Cleaning & feature prep (pandas) → 3. EDA (KPIs, trends, category/region/product, discount impact)
→ 4. Modelling: Random Forest (profit prediction, R²/MAE on 20% test set) + Linear Regression with trend+seasonality (6-month sales forecast)
→ 5. Deployment: Flask REST APIs + HTML/Chart.js dashboard.

## Run
```
pip install -r requirements.txt
python generate_data.py
python app.py        # open http://127.0.0.1:5000
```

## Key insights to mention in report
- Sales grow year over year and peak in Nov–Dec (seasonality).
- Technology has the highest sales; Office Supplies the best margin; Furniture the lowest.
- Higher discounts sharply reduce average profit per order (above ~20-30% it turns negative for low-margin items).

## Structure
`app.py` (backend + ML) · `templates/index.html` (frontend) · `generate_data.py` · `data/` · `requirements.txt`

## Future scope
Customer segmentation (K-Means), database (SQLite), user upload of CSV, model deployment on cloud.
