# 🧠 Startup Intelligence Dashboard

> AI-powered e-commerce analytics platform with automated business insights, customer segmentation, anomaly detection, and growth strategy recommendations — built entirely with Python, no external AI API required.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=flat&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 📌 Overview

**Startup Intelligence Dashboard** is a full-featured business analytics platform designed for e-commerce operators and startup founders. It transforms raw transaction data into actionable insights through automated AI analysis, customer segmentation, funnel diagnostics, and interactive what-if revenue projections.

Built as a single-file Streamlit app with zero dependency on external AI APIs — all intelligence is computed in pure Python.

---

## ✨ Features

### 📊 Overview Tab
- Monthly revenue bar charts and daily active user trends
- Top products by quantity and top countries by revenue
- Conversion funnel visualization
- Order volume heatmap by day of week and hour

### 🧠 AI Analyst Tab
- **Automated insight cards** — auto-detects revenue instability, ARPU gaps, churn risk, geographic concentration, and seasonality
- **Revenue anomaly detection** — flags statistical outliers using z-score analysis (±2σ)
- **Interactive Q&A engine** — ask natural language business questions and get structured, data-driven answers

### 👥 Customer Intelligence Tab
- **RFM Segmentation** — classifies customers into Champions, Loyal, At Risk, and Lost using Recency, Frequency, and Monetary scores
- Segment summary cards with revenue attribution
- RFM scatter plot and revenue treemap by segment
- Top 15 most valuable customers table
- Weekly retention cohort heatmap

### 📉 Sales Diagnostics Tab
- Month-over-month waterfall chart for revenue changes
- Country ARPU benchmarking vs. dataset average
- Product velocity scatter plot (volume vs. revenue vs. order count)
- Funnel drop-off analysis with step-by-step conversion and drop percentages

### 🚀 Growth Opportunities Tab
- Prioritised action cards (P1–P4) with effort/impact ratings and step-by-step playbooks
- **Interactive revenue projection** — sliders for retention lift, AOV increase, and user growth
- Combined uplift scenario with projected annual revenue output

---

## 🗂 Project Structure

```
startup-intelligence/
├── app/
│   └── dashboard.py          # Main Streamlit application
├── data/
│   ├── raw/                  # Source data files
│   └── processed/
│       ├── processed_data.csv
│       └── funnel.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/startup-intelligence.git
cd startup-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your data

Place your processed CSV files in `data/processed/`:

- `processed_data.csv` — transaction data with columns: `InvoiceDate`, `Invoice`, `Customer ID`, `Description`, `Quantity`, `Price`, `Country`
- `funnel.csv` — funnel steps with columns: `Step`, `Count`

### 5. Run the dashboard

```bash
streamlit run app/dashboard.py
```

---

## 📦 Requirements

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.15.0
```

Generate `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## 📈 Dataset

This project was developed and tested using the **Online Retail II** dataset (UCI Machine Learning Repository), containing UK-based e-commerce transactions from 2009–2011.

| Field        | Description                        |
|--------------|------------------------------------|
| InvoiceDate  | Transaction timestamp              |
| Invoice      | Unique order identifier            |
| Customer ID  | Unique customer identifier         |
| Description  | Product name                       |
| Quantity     | Units purchased                    |
| Price        | Unit price (GBP)                   |
| Country      | Customer country                   |

---

## 🧩 How the AI Engine Works

All analysis is computed in pure Python — no OpenAI, Anthropic, or any external API calls.

| Module | Method |
|---|---|
| Revenue pattern detection | Trend analysis + MoM % change |
| ARPU & retention benchmarking | Rule-based threshold classification |
| Anomaly detection | Z-score (±2 standard deviations) |
| RFM segmentation | Quantile-based scoring with robust fallback |
| Q&A engine | Keyword intent matching + metric-driven responses |
| Growth projections | Parametric what-if modelling with sliders |

---

## 🖥 Dashboard Filters

Use the sidebar to filter data dynamically:

- **Countries** — multi-select filter for geographic analysis
- **Date Range** — restrict analysis to a specific time window
- **Analysis Mode** — switch between Overview, AI Analyst, Customer Intelligence, Sales Diagnostics, and Growth Opportunities

All charts, KPIs, and AI insights update in real time based on active filters.

---

## 📸 Screenshots

> *(Add screenshots of each tab here)*

| Overview | AI Analyst | Customer Intelligence |
|---|---|---|
| ![Overview](#) | ![AI Analyst](#) | ![Customers](#) |

---

## 🤝 Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Author

**Aditya**

Built with Streamlit · Plotly · Python Analytics

---

> ⭐ If you found this project useful, consider giving it a star on GitHub!
