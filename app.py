"""Flask backend: loads the dataset, does analysis with pandas, trains ML models, serves JSON APIs."""
import numpy as np, pandas as pd
from flask import Flask, jsonify, render_template, request
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

app = Flask(__name__)
df = pd.read_csv("data/retail_sales.csv", parse_dates=["order_date"])
df["month"] = df["order_date"].dt.to_period("M")

# ---- Model 1: Random Forest to predict order profit ----
FEATS = ["category", "region", "segment", "quantity", "discount", "unit_price"]
X = pd.get_dummies(df[FEATS]); y = df["profit"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.2, random_state=42)
rf = RandomForestRegressor(200, random_state=42).fit(Xtr, ytr)
pred = rf.predict(Xte)
MODEL_INFO = {"r2": round(r2_score(yte, pred), 3), "mae": round(mean_absolute_error(yte, pred), 2)}

# ---- Model 2: Linear trend + seasonality to forecast monthly sales ----
monthly = df.groupby("month")["sales"].sum()
def design(t, mo): return np.column_stack([t, np.eye(12)[mo - 1]])
t = np.arange(len(monthly))
lr = LinearRegression().fit(design(t, monthly.index.month.values), monthly.values)

@app.route("/")
def index(): return render_template("index.html")

@app.route("/api/kpis")
def kpis():
    return jsonify(sales=round(df.sales.sum()), profit=round(df.profit.sum()), orders=len(df),
                   margin=round(df.profit.sum() / df.sales.sum() * 100, 1), avg_order=round(df.sales.mean(), 2))

@app.route("/api/monthly")
def api_monthly():
    g = df.groupby("month")[["sales", "profit"]].sum().round(0)
    return jsonify(labels=g.index.astype(str).tolist(), sales=g.sales.tolist(), profit=g.profit.tolist())

@app.route("/api/by/<col>")
def by(col):
    if col not in ("category", "region", "segment", "product"): return jsonify(error="bad column"), 400
    g = df.groupby(col)[["sales", "profit"]].sum().round(0).sort_values("sales", ascending=False)
    return jsonify(labels=g.index.tolist(), sales=g.sales.tolist(), profit=g.profit.tolist())

@app.route("/api/discount")
def discount():
    g = df.groupby("discount")["profit"].mean().round(2)
    return jsonify(labels=[f"{int(d*100)}%" for d in g.index], profit=g.tolist())

@app.route("/api/forecast")
def forecast():
    last = monthly.index[-1]; fut = pd.period_range(last + 1, periods=6, freq="M")
    fp = lr.predict(design(np.arange(len(monthly), len(monthly) + 6), fut.month.values))
    return jsonify(labels=monthly.index.astype(str).tolist() + fut.astype(str).tolist(),
                   actual=monthly.round(0).tolist() + [None] * 6,
                   forecast=[None] * (len(monthly) - 1) + [round(monthly.iloc[-1])] + fp.round(0).tolist())

@app.route("/api/options")
def options():
    return jsonify({c: sorted(df[c].unique().tolist()) for c in ["category", "region", "segment"]}, ) 

@app.route("/api/model_info")
def model_info(): return jsonify(MODEL_INFO)

@app.route("/api/predict", methods=["POST"])
def predict():
    d = request.get_json()
    row = pd.DataFrame([{k: d[k] for k in FEATS}])
    for c in ("quantity", "discount", "unit_price"): row[c] = pd.to_numeric(row[c])
    row = pd.get_dummies(row).reindex(columns=X.columns, fill_value=0)
    return jsonify(profit=round(float(rf.predict(row)[0]), 2))

if __name__ == "__main__":
    app.run(debug=True)
