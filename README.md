# CodeClauseInternship_CLVP
# Customer Lifetime Value Prediction App

## Project Overview

This project predicts **Customer Lifetime Value (CLV)** using real transaction data from the Online Retail dataset.
It combines regression modeling with a web-based Flask application to allow businesses to estimate how much value a customer will bring over their lifetime.

---

## Key Features

- Uses real business data to calculate:
  - **Average Order Value (AOV)**
  - **Purchase Frequency**
  - **Customer Lifespan**
- Predicts **CLV** using a trained machine learning model
- Fully interactive **Flask-based UI**

---

## Machine Learning Pipeline

- Feature Engineering:
  - AOV = TotalRevenue / TotalOrders
  - Frequency = Orders / Customers
  - Lifespan = Time difference between first and last invoice
- Model: `LinearRegression` (scikit-learn)
- Target: Predicted CLV

---

## Flask App

### User Inputs
- Average Order Value 
- Purchase Frequency 
- Customer Lifespan in months
### 🎯 Output
- Estimated CLV

---

## 💻 How to Run

1. Clone the repo:
```bash
git clone https://github.com/your-username/clv-flask-app
cd clv-flask-app

