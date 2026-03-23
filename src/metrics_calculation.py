# src/metrics_calculation.py

import os
import pandas as pd

# --- Setup paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
processed_file = os.path.join(BASE_DIR, "data", "processed", "processed_data.csv")

# Outputs
dau_file = os.path.join(BASE_DIR, "data", "processed", "dau.csv")
wau_file = os.path.join(BASE_DIR, "data", "processed", "wau.csv")
mau_file = os.path.join(BASE_DIR, "data", "processed", "mau.csv")
retention_file = os.path.join(BASE_DIR, "data", "processed", "retention.csv")
funnel_file = os.path.join(BASE_DIR, "data", "processed", "funnel.csv")
revenue_file = os.path.join(BASE_DIR, "data", "processed", "revenue.csv")
top_products_file = os.path.join(BASE_DIR, "data", "processed", "top_products.csv")
top_countries_file = os.path.join(BASE_DIR, "data", "processed", "top_countries.csv")

# --- Load cleaned data ---
df = pd.read_csv(processed_file, parse_dates=['InvoiceDate'])

# --- DAU (Daily Active Users) ---
dau = df.groupby('day')['Customer ID'].nunique().reset_index()
dau.rename(columns={'Customer ID': 'DAU'}, inplace=True)
dau.to_csv(dau_file, index=False)

# --- WAU (Weekly Active Users) ---
df['week'] = df['InvoiceDate'].dt.isocalendar().week
wau = df.groupby('week')['Customer ID'].nunique().reset_index()
wau.rename(columns={'Customer ID': 'WAU'}, inplace=True)
wau.to_csv(wau_file, index=False)

# --- MAU (Monthly Active Users) ---
df['month'] = df['InvoiceDate'].dt.to_period('M')
mau = df.groupby('month')['Customer ID'].nunique().reset_index()
mau.rename(columns={'Customer ID': 'MAU'}, inplace=True)
mau.to_csv(mau_file, index=False)

# --- Retention Cohorts (weekly) ---
user_week = df.groupby(['Customer ID', 'week']).size().reset_index(name='activity_count')
retention = user_week.pivot_table(index='Customer ID', columns='week', values='activity_count', fill_value=0)
retention.to_csv(retention_file)

# --- Conversion Funnel ---
total_orders = df.shape[0]
unique_users = df['Customer ID'].nunique()
# For simplicity, assume visits = unique users * 1.5 (you can replace with actual data)
visits = int(unique_users * 1.5)
funnel = pd.DataFrame({
    'Step': ['Visits', 'Unique Users', 'Total Orders'],
    'Count': [visits, unique_users, total_orders],
    'Conversion Rate (%)': [100, round(unique_users/visits*100,2), round(total_orders/visits*100,2)]
})
funnel.to_csv(funnel_file, index=False)

# --- Revenue Metrics ---
df['Revenue'] = df['Quantity'] * df['Price']
monthly_revenue = df.groupby('month')['Revenue'].sum().reset_index()
arpu = df.groupby('Customer ID')['Revenue'].sum().mean()
monthly_revenue.to_csv(revenue_file, index=False)

# --- Top Products ---
top_products = df.groupby('StockCode')['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False).head(10)
top_products.to_csv(top_products_file, index=False)

# --- Top Countries ---
top_countries = df.groupby('Country')['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False).head(10)
top_countries.to_csv(top_countries_file, index=False)

print("✅ All metrics calculated and saved to processed folder.")
print(f"✅ ARPU: {arpu:.2f}")