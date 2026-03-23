"""
╔══════════════════════════════════════════════════════════════════╗
║       STARTUP METRICS — ELITE AI INTELLIGENCE DASHBOARD         ║
║  · AI Business Analyst  · Pattern Detection  · Smart Q&A        ║
╚══════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px
import plotly.graph_objects as go
from datetime import timedelta

# ══════════════════════════════════════════════
# PAGE CONFIG
# ══════════════════════════════════════════════
st.set_page_config(
    page_title="Startup Metrics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🧠",
)

# ══════════════════════════════════════════════
# ELITE CSS
# ══════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap');

:root {
    --bg:       #060F1E;
    --card:     #0B1525;
    --card2:    #0E1C32;
    --border:   rgba(99,179,237,0.12);
    --glow:     rgba(99,179,237,0.4);
    --blue:     #63B3ED;
    --cyan:     #4FD1C5;
    --purple:   #B794F4;
    --green:    #68D391;
    --orange:   #F6AD55;
    --red:      #FC8181;
    --yellow:   #F6E05E;
    --txt:      #EDF2F7;
    --txt2:     #A0AEC0;
    --txt3:     #4A5568;
    --mono:     'Space Mono', monospace;
    --sans:     'DM Sans', sans-serif;
}

html, body, [class*="css"] {
    font-family: var(--sans) !important;
    background-color: var(--bg) !important;
    color: var(--txt) !important;
}
.stApp {
    background: var(--bg) !important;
    background-image:
        radial-gradient(ellipse at 5% 5%,   rgba(99,179,237,.08)  0%, transparent 50%),
        radial-gradient(ellipse at 95% 90%,  rgba(183,148,244,.06) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%,  rgba(79,209,197,.03)  0%, transparent 70%) !important;
}

::-webkit-scrollbar            { width:4px; height:4px; }
::-webkit-scrollbar-track      { background:var(--bg); }
::-webkit-scrollbar-thumb      { background:rgba(99,179,237,.25); border-radius:2px; }
.block-container                { padding:0 2.5rem 3rem !important; max-width:1800px !important; }

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background:#060E1C !important;
    border-right:1px solid var(--border) !important;
}
section[data-testid="stSidebar"] .block-container { padding:1.8rem 1rem !important; }
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p {
    color:var(--txt2) !important; font-size:.7rem !important;
    font-weight:600 !important; letter-spacing:.08em !important;
    text-transform:uppercase !important;
}
section[data-testid="stSidebar"] .stRadio label {
    color:var(--txt) !important; font-size:.82rem !important;
    text-transform:none !important; letter-spacing:0 !important;
    font-weight:500 !important;
}

#MainMenu, footer, header { visibility:hidden !important; }

/* ── HEADER ── */
.dash-header {
    padding:2rem 0 1.2rem; border-bottom:1px solid var(--border);
    margin-bottom:1.8rem; position:relative;
}
.dash-header::after {
    content:''; position:absolute; bottom:-1px; left:0;
    width:80px; height:2px;
    background:linear-gradient(90deg,var(--blue),var(--cyan));
}
.dash-title {
    font-family:var(--mono) !important; font-size:1.9rem !important;
    font-weight:700 !important;
    background:linear-gradient(120deg,#EDF2F7 20%,var(--blue) 100%);
    -webkit-background-clip:text !important;
    -webkit-text-fill-color:transparent !important;
    line-height:1.2 !important; margin:0 !important;
}
.dash-sub {
    color:var(--txt3) !important; font-size:.7rem !important;
    letter-spacing:.14em !important; text-transform:uppercase !important;
    margin-top:.3rem !important;
}
.live-pill {
    display:inline-flex; align-items:center; gap:5px;
    background:rgba(104,211,145,.1); border:1px solid rgba(104,211,145,.3);
    border-radius:20px; padding:3px 10px; font-size:.62rem; font-weight:700;
    color:var(--green); letter-spacing:.1em; text-transform:uppercase;
    vertical-align:middle; margin-left:.7rem;
}
.live-pill::before {
    content:''; width:5px; height:5px; background:var(--green);
    border-radius:50%; animation:blink 2s infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:.3;transform:scale(1.4)} }

/* ── KPI CARDS ── */
.kpi-wrap {
    background:var(--card); border:1px solid var(--border);
    border-radius:14px; padding:1.3rem 1.2rem 1.1rem;
    position:relative; overflow:hidden;
    transition:all .25s ease; min-height:155px; box-sizing:border-box;
}
.kpi-wrap:hover {
    border-color:var(--glow); transform:translateY(-3px);
    box-shadow:0 16px 48px rgba(99,179,237,.1);
}
.kpi-wrap::before {
    content:''; position:absolute; top:0; left:0; right:0; height:2px;
    background:var(--kpi-grad, linear-gradient(90deg,var(--blue),var(--cyan)));
}
.kpi-orb {
    position:absolute; bottom:-16px; right:-16px;
    width:65px; height:65px; border-radius:50%;
    background:var(--kpi-gc, var(--blue)); opacity:.07; filter:blur(18px);
}
.kpi-icon  { font-size:1.2rem; display:block; margin-bottom:.6rem; }
.kpi-lbl   { font-size:.6rem; font-weight:700; color:var(--txt3);
             letter-spacing:.12em; text-transform:uppercase; margin-bottom:.28rem; }
.kpi-val   {
    font-family:var(--mono); font-weight:700; color:var(--txt);
    font-size:clamp(.9rem,1.55vw,1.6rem); line-height:1.1;
    margin-bottom:.4rem; word-break:break-all; overflow-wrap:break-word;
}
.kpi-delta    { font-size:.66rem; font-weight:500; }
.kpi-delta.up { color:var(--green); }
.kpi-delta.dn { color:var(--red); }
.kpi-delta.nt { color:var(--txt3); }

/* ── SECTION HEADER ── */
.sec-head {
    display:flex; align-items:center; gap:10px;
    margin:2.5rem 0 1.1rem; padding-bottom:.7rem;
    border-bottom:1px solid var(--border);
}
.sec-title {
    font-family:var(--mono) !important; font-size:.75rem !important;
    font-weight:700 !important; letter-spacing:.1em !important;
    text-transform:uppercase !important; color:var(--txt2) !important;
    white-space:nowrap;
}
.sec-line { flex:1; height:1px; background:linear-gradient(90deg,var(--border),transparent); }
.sec-badge {
    font-size:.6rem; font-weight:700; padding:2px 8px;
    border-radius:10px; letter-spacing:.08em; text-transform:uppercase;
}

/* ── AI INSIGHT CARDS ── */
.ai-card {
    border-radius:13px; padding:1.1rem 1.3rem;
    margin-bottom:.7rem; position:relative; overflow:hidden;
}
.ai-card.critical {
    background:linear-gradient(135deg,rgba(252,129,129,.1),rgba(252,129,129,.04));
    border:1px solid rgba(252,129,129,.25);
}
.ai-card.warning {
    background:linear-gradient(135deg,rgba(246,173,85,.1),rgba(246,173,85,.04));
    border:1px solid rgba(246,173,85,.25);
}
.ai-card.positive {
    background:linear-gradient(135deg,rgba(104,211,145,.1),rgba(104,211,145,.04));
    border:1px solid rgba(104,211,145,.25);
}
.ai-card.info {
    background:linear-gradient(135deg,rgba(99,179,237,.1),rgba(99,179,237,.04));
    border:1px solid rgba(99,179,237,.25);
}
.ai-card-badge {
    font-size:.58rem; font-weight:700; letter-spacing:.1em; text-transform:uppercase;
    padding:2px 8px; border-radius:8px; margin-bottom:.5rem; display:inline-block;
}
.ai-card.critical .ai-card-badge { background:rgba(252,129,129,.2); color:#FC8181; }
.ai-card.warning  .ai-card-badge { background:rgba(246,173,85,.2);  color:#F6AD55; }
.ai-card.positive .ai-card-badge { background:rgba(104,211,145,.2); color:#68D391; }
.ai-card.info     .ai-card-badge { background:rgba(99,179,237,.2);  color:#63B3ED; }
.ai-card-title {
    font-size:.92rem; font-weight:700; color:var(--txt);
    margin-bottom:.35rem; line-height:1.3;
}
.ai-card-body { font-size:.82rem; color:var(--txt2); line-height:1.6; }
.ai-card-action {
    margin-top:.6rem; font-size:.78rem; font-weight:600; color:var(--blue);
    border-top:1px solid rgba(99,179,237,.12); padding-top:.5rem;
}

/* ── AI Q&A ── */
.qa-question {
    background:rgba(99,179,237,.08); border:1px solid rgba(99,179,237,.2);
    border-radius:12px; padding:.8rem 1.1rem; font-size:.88rem;
    color:var(--blue); font-weight:600; cursor:pointer; margin-bottom:.5rem;
    transition:all .2s;
}
.qa-question:hover { background:rgba(99,179,237,.14); border-color:rgba(99,179,237,.4); }
.qa-answer {
    background:var(--card2); border:1px solid var(--border);
    border-radius:12px; padding:1.1rem 1.3rem;
    font-size:.85rem; color:var(--txt2); line-height:1.7;
    margin-bottom:1rem;
}
.qa-answer b { color:var(--txt); }

/* ── CUSTOMER SEGMENT CARDS ── */
.seg-card {
    background:var(--card); border:1px solid var(--border);
    border-radius:13px; padding:1.1rem 1.2rem; text-align:center;
}
.seg-val   { font-family:var(--mono); font-size:1.5rem; font-weight:700; color:var(--txt); }
.seg-lbl   { font-size:.65rem; color:var(--txt3); text-transform:uppercase;
             letter-spacing:.1em; margin-top:.3rem; }
.seg-pct   { font-size:.78rem; font-weight:600; margin-top:.4rem; }

/* ── ANOMALY BADGE ── */
.anomaly-row {
    display:flex; align-items:center; gap:12px; padding:.6rem 0;
    border-bottom:1px solid var(--border); font-size:.83rem;
}
.anomaly-row:last-child { border-bottom:none; }

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background:transparent !important; gap:.5rem;
    border-bottom:1px solid var(--border) !important;
}
.stTabs [data-baseweb="tab"] {
    background:transparent !important; color:var(--txt3) !important;
    border:none !important; border-radius:8px 8px 0 0 !important;
    font-family:var(--mono) !important; font-size:.7rem !important;
    font-weight:700 !important; letter-spacing:.08em !important;
    text-transform:uppercase !important; padding:.5rem 1rem !important;
}
.stTabs [aria-selected="true"] {
    color:var(--blue) !important;
    border-bottom:2px solid var(--blue) !important;
}
.stTabs [data-baseweb="tab-panel"] { padding:1.5rem 0 0 !important; }

/* ── TEXT AREA / INPUT ── */
.stTextArea textarea, .stTextInput input {
    background:var(--card2) !important; border:1px solid var(--border) !important;
    color:var(--txt) !important; border-radius:10px !important;
    font-family:var(--sans) !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color:var(--blue) !important;
    box-shadow:0 0 0 2px rgba(99,179,237,.2) !important;
}

/* ── BUTTONS ── */
.stButton button {
    background:linear-gradient(135deg,rgba(99,179,237,.15),rgba(79,209,197,.1)) !important;
    border:1px solid rgba(99,179,237,.3) !important; color:var(--blue) !important;
    font-family:var(--mono) !important; font-size:.72rem !important;
    font-weight:700 !important; letter-spacing:.08em !important;
    border-radius:10px !important; padding:.5rem 1.2rem !important;
    text-transform:uppercase !important; transition:all .2s !important;
}
.stButton button:hover {
    background:linear-gradient(135deg,rgba(99,179,237,.25),rgba(79,209,197,.15)) !important;
    border-color:rgba(99,179,237,.6) !important;
    box-shadow:0 4px 20px rgba(99,179,237,.2) !important;
}

/* ── SELECT BOX ── */
.stSelectbox [data-baseweb="select"] div {
    background:var(--card2) !important; border:1px solid var(--border) !important;
    color:var(--txt) !important; border-radius:10px !important;
}

.dash-footer {
    text-align:center; padding:2rem 0; color:var(--txt3); font-size:.7rem;
    letter-spacing:.1em; text-transform:uppercase;
    border-top:1px solid var(--border); margin-top:3rem;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# PLOTLY THEME
# ══════════════════════════════════════════════
_PL = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans, sans-serif", color="#A0AEC0", size=12),
    title_font=dict(family="Space Mono, monospace", color="#EDF2F7", size=13),
    xaxis=dict(gridcolor="rgba(99,179,237,0.06)", linecolor="rgba(99,179,237,0.1)",
               tickfont=dict(color="#718096"), zerolinecolor="rgba(99,179,237,0.06)"),
    yaxis=dict(gridcolor="rgba(99,179,237,0.06)", linecolor="rgba(99,179,237,0.1)",
               tickfont=dict(color="#718096"), zerolinecolor="rgba(99,179,237,0.06)"),
    margin=dict(l=20, r=20, t=50, b=20),
    hoverlabel=dict(bgcolor="#0B1525", bordercolor="rgba(99,179,237,0.4)",
                    font=dict(color="#EDF2F7", family="DM Sans")),
)
_DEF_LEGEND = dict(bgcolor="rgba(11,21,37,0.9)", bordercolor="rgba(99,179,237,0.18)",
                   borderwidth=1, font=dict(color="#A0AEC0"))
PAL = ["#63B3ED", "#4FD1C5", "#B794F4", "#68D391", "#F6AD55", "#FC8181", "#F6E05E"]


def T(fig, title="", legend=None):
    fig.update_layout(**_PL, legend=legend or _DEF_LEGEND)
    if title:
        fig.update_layout(title_text=title)
    return fig


def sec(title, badge=None, badge_color="#63B3ED"):
    badge_html = ""
    if badge:
        bg = badge_color.replace("#", "")
        badge_html = (f"<span class='sec-badge' style='background:rgba({int(bg[:2],16)},"
                      f"{int(bg[2:4],16)},{int(bg[4:],16)},.15);color:{badge_color};'>"
                      f"{badge}</span>")
    st.markdown(
        f"<div class='sec-head'><span class='sec-title'>{title}</span>"
        f"{badge_html}<div class='sec-line'></div></div>",
        unsafe_allow_html=True)


# ══════════════════════════════════════════════
# DATA LOAD
# ══════════════════════════════════════════════
BASE_DIR       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
processed_file = os.path.join(BASE_DIR, "data", "processed", "processed_data.csv")
funnel_file    = os.path.join(BASE_DIR, "data", "processed", "funnel.csv")


@st.cache_data
def load_data():
    df_raw = pd.read_csv(processed_file, parse_dates=["InvoiceDate"])
    funnel = pd.read_csv(funnel_file)
    return df_raw, funnel


df_raw, funnel = load_data()
df_raw["Revenue"] = df_raw["Quantity"] * df_raw["Price"]
df_raw["month"]   = df_raw["InvoiceDate"].dt.to_period("M").astype(str)
df_raw["day"]     = df_raw["InvoiceDate"].dt.date
df_raw["week"]    = df_raw["InvoiceDate"].dt.to_period("W").astype(str)
df_raw["hour"]    = df_raw["InvoiceDate"].dt.hour
df_raw["dow"]     = df_raw["InvoiceDate"].dt.day_name()


# ══════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
<div style='margin-bottom:1.5rem;'>
  <div style='font-family:Space Mono,monospace;font-size:.95rem;font-weight:700;
              color:#63B3ED;letter-spacing:.04em;'>&#9635; INTELLIGENCE HUB</div>
  <div style='font-size:.62rem;color:#4A5568;margin-top:3px;
              letter-spacing:.1em;text-transform:uppercase;'>AI-Powered Business Analytics</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("**&#127758; Countries**")
    countries = st.multiselect(
        "Countries", options=sorted(df_raw["Country"].dropna().unique()),
        default=list(df_raw["Country"].dropna().unique()),
        label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**&#128197; Date Range**")
    date_range = st.date_input(
        "Date Range",
        value=[df_raw["InvoiceDate"].min().date(), df_raw["InvoiceDate"].max().date()],
        label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**&#127775; Analysis Mode**")
    mode = st.radio("Mode", ["Overview", "AI Analyst", "Customer Intelligence",
                              "Sales Diagnostics", "Growth Opportunities"],
                    label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div style='background:rgba(99,179,237,.05);border:1px solid rgba(99,179,237,.13);
            border-radius:10px;padding:.85rem;'>
  <div style='font-size:.6rem;color:#4A5568;letter-spacing:.1em;
              text-transform:uppercase;margin-bottom:.35rem;'>Dataset</div>
  <div style='font-size:.78rem;color:#A0AEC0;'>E-Commerce Transactions</div>
  <div style='font-size:.62rem;color:#4A5568;margin-top:.2rem;'>UK Retail · 2009-2011</div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# FILTER DATA
# ══════════════════════════════════════════════
if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
    d0, d1 = date_range[0], date_range[1]
else:
    d0 = d1 = (date_range[0] if hasattr(date_range, "__len__") else date_range)

df = df_raw[
    (df_raw["Country"].isin(countries)) &
    (df_raw["InvoiceDate"].dt.date >= d0) &
    (df_raw["InvoiceDate"].dt.date <= d1)
].copy()


# ══════════════════════════════════════════════
# CORE KPI CALCULATIONS
# ══════════════════════════════════════════════
total_users   = int(df["Customer ID"].nunique())
total_orders  = int(df["Invoice"].nunique()) if "Invoice" in df.columns else int(len(df))
total_revenue = float(df["Revenue"].sum())
arpu          = total_revenue / total_users  if total_users  > 0 else 0.0
aov           = total_revenue / total_orders if total_orders > 0 else 0.0

monthly_rev   = df.groupby("month")["Revenue"].sum().reset_index()
growth = 0.0
if len(monthly_rev) > 1 and monthly_rev.iloc[0]["Revenue"] != 0:
    growth = ((monthly_rev.iloc[-1]["Revenue"] - monthly_rev.iloc[0]["Revenue"])
              / monthly_rev.iloc[0]["Revenue"]) * 100

# MoM last two months
mom_change = 0.0
if len(monthly_rev) >= 2:
    prev = monthly_rev.iloc[-2]["Revenue"]
    curr = monthly_rev.iloc[-1]["Revenue"]
    mom_change = ((curr - prev) / prev * 100) if prev != 0 else 0.0

# Repeat purchase rate
cust_orders = df.groupby("Customer ID")["month"].nunique()
repeat_rate = float((cust_orders > 1).sum() / len(cust_orders) * 100) if len(cust_orders) > 0 else 0.0


# ══════════════════════════════════════════════
# AI ANALYSIS ENGINE
# ══════════════════════════════════════════════
@st.cache_data
def run_ai_analysis(data_hash, _df, _monthly_rev, _funnel, _growth, _arpu, _repeat_rate, _mom):
    """Pure Python AI analysis — no external API needed."""
    insights = []
    actions  = []

    # ── Revenue Pattern Analysis ──
    if len(_monthly_rev) >= 3:
        rev_vals   = _monthly_rev["Revenue"].values
        rev_pct    = np.diff(rev_vals) / np.where(rev_vals[:-1] == 0, 1, rev_vals[:-1]) * 100
        neg_months = (rev_pct < -10).sum()
        best_m     = _monthly_rev.loc[_monthly_rev["Revenue"].idxmax()]
        worst_m    = _monthly_rev.loc[_monthly_rev["Revenue"].idxmin()]
        ratio      = best_m["Revenue"] / worst_m["Revenue"] if worst_m["Revenue"] > 0 else 1

        if neg_months >= 2:
            insights.append({
                "type": "critical",
                "title": "Revenue Instability Detected",
                "body": (f"Revenue dropped >10% in {neg_months} months. "
                         f"Peak was <b>${best_m['Revenue']:,.0f}</b> ({best_m['month']}) vs "
                         f"low of <b>${worst_m['Revenue']:,.0f}</b> ({worst_m['month']}). "
                         f"That's a <b>{ratio:.1f}x</b> swing — high volatility."),
                "action": "&#128073; Fix: Introduce subscription/recurring revenue to smooth volatility. "
                          "Identify what drove peak month and replicate those conditions."
            })
        elif _growth < 0:
            insights.append({
                "type": "warning",
                "title": "Declining Revenue Trend",
                "body": (f"Overall growth is <b>{_growth:.1f}%</b>. Last month changed "
                         f"<b>{_mom:+.1f}%</b> MoM. Revenue is trending downward."),
                "action": "&#128073; Fix: Run a win-back campaign for churned customers. "
                          "Review pricing — a 5% price increase can outperform 20% volume growth."
            })
        else:
            insights.append({
                "type": "positive",
                "title": "Revenue Growing Steadily",
                "body": (f"Business is growing at <b>{_growth:.1f}%</b> overall. "
                         f"Last MoM change: <b>{_mom:+.1f}%</b>. "
                         f"Peak month <b>{best_m['month']}</b> hit <b>${best_m['Revenue']:,.0f}</b>."),
                "action": "&#128073; Opportunity: Double down on what made "
                          f"{best_m['month']} successful. Scale those channels."
            })

    # ── ARPU Analysis ──
    if _arpu < 30:
        insights.append({
            "type": "critical",
            "title": "Critically Low ARPU ($" + f"{_arpu:.2f})",
            "body": (f"Average revenue per user is only <b>${_arpu:.2f}</b>. "
                     "This means you need very high volume to be profitable. "
                     "Customer acquisition costs likely exceed lifetime value."),
            "action": "&#128073; Fix: Bundle products, introduce tiered pricing, add premium SKUs. "
                      "A 2x ARPU improvement doubles revenue without acquiring new customers."
        })
    elif _arpu < 100:
        insights.append({
            "type": "warning",
            "title": f"ARPU Has Room to Grow (${_arpu:.2f})",
            "body": (f"ARPU of <b>${_arpu:.2f}</b> is below benchmark for e-commerce (~$150+). "
                     "Customers are under-monetised relative to their visit frequency."),
            "action": "&#128073; Fix: Cross-sell related products at checkout. "
                      "Top 20% of customers likely drive 80% of revenue — find and clone them."
        })
    else:
        insights.append({
            "type": "positive",
            "title": f"Healthy ARPU (${_arpu:.2f})",
            "body": f"Strong revenue per user at <b>${_arpu:.2f}</b>. Focus on growing customer count.",
            "action": "&#128073; Opportunity: Invest in acquisition — your monetisation is working."
        })

    # ── Retention Analysis ──
    if _repeat_rate < 30:
        insights.append({
            "type": "critical",
            "title": f"Severe Churn Problem ({_repeat_rate:.1f}% repeat buyers)",
            "body": (f"Only <b>{_repeat_rate:.1f}%</b> of customers return for a second purchase. "
                     "You're running a leaky bucket — spending to acquire customers who leave immediately. "
                     "Fixing retention has 5-7x better ROI than acquisition."),
            "action": "&#128073; Fix: Launch email sequence 3/7/14 days post-purchase. "
                      "Add loyalty points. First-repeat-purchase discount (10% off 2nd order). "
                      "Target: get repeat rate to 40%+ within 90 days."
        })
    elif _repeat_rate < 50:
        insights.append({
            "type": "warning",
            "title": f"Retention Needs Improvement ({_repeat_rate:.1f}% repeat)",
            "body": (f"<b>{_repeat_rate:.1f}%</b> repeat purchase rate. "
                     "Industry leaders achieve 60-70%. There's meaningful LTV being left on the table."),
            "action": "&#128073; Fix: Personalised product recommendations based on past purchases. "
                      "Win-back campaign for customers inactive 60+ days."
        })
    else:
        insights.append({
            "type": "positive",
            "title": f"Strong Retention ({_repeat_rate:.1f}% repeat buyers)",
            "body": (f"<b>{_repeat_rate:.1f}%</b> of customers make repeat purchases. "
                     "Your product-market fit is strong."),
            "action": "&#128073; Opportunity: Build a referral programme — "
                      "loyal customers are your cheapest acquisition channel."
        })

    # ── Country Concentration Risk ──
    country_rev = _df.groupby("Country")["Revenue"].sum()
    top_country_pct = country_rev.max() / country_rev.sum() * 100 if country_rev.sum() > 0 else 0
    top_country     = country_rev.idxmax() if not country_rev.empty else "N/A"
    if top_country_pct > 70:
        insights.append({
            "type": "warning",
            "title": f"Geographic Concentration Risk",
            "body": (f"<b>{top_country_pct:.0f}%</b> of revenue comes from <b>{top_country}</b>. "
                     "A single market dependency is a major business risk."),
            "action": "&#128073; Fix: Localise marketing for top 3 underperforming countries. "
                      "Translate product pages, accept local payment methods."
        })

    # ── Seasonality Detection ──
    if len(_monthly_rev) >= 6:
        rev_std  = _monthly_rev["Revenue"].std()
        rev_mean = _monthly_rev["Revenue"].mean()
        cv       = rev_std / rev_mean if rev_mean > 0 else 0
        if cv > 0.3:
            peak_m = _monthly_rev.loc[_monthly_rev["Revenue"].idxmax(), "month"]
            insights.append({
                "type": "info",
                "title": "Strong Seasonality Pattern Detected",
                "body": (f"Revenue coefficient of variation is <b>{cv:.1%}</b> — high seasonality. "
                         f"Peak is around <b>{peak_m}</b>. "
                         "Seasonal businesses need off-peak revenue strategies."),
                "action": "&#128073; Strategy: Pre-sell inventory before peak. "
                          "Create off-season promotions. Build a waitlist during slow months."
            })

    # ── Funnel Drop Analysis ──
    if len(_funnel) >= 2:
        _funnel_r = _funnel.reset_index(drop=True)
        worst_drop_idx  = 0
        worst_drop_pct  = 0.0
        for i in range(1, len(_funnel_r)):
            prev_count = _funnel_r.loc[i-1, "Count"]
            curr_count = _funnel_r.loc[i,   "Count"]
            if prev_count > 0:
                drop = (prev_count - curr_count) / prev_count * 100
                if drop > worst_drop_pct:
                    worst_drop_pct = drop
                    worst_drop_idx = i
        if worst_drop_pct > 30:
            step_name = _funnel_r.loc[worst_drop_idx, "Step"]
            prev_name = _funnel_r.loc[worst_drop_idx - 1, "Step"]
            insights.append({
                "type": "critical",
                "title": f"Major Funnel Leak: {prev_name} → {step_name}",
                "body": (f"<b>{worst_drop_pct:.0f}%</b> of users drop off between "
                         f"<b>{prev_name}</b> and <b>{step_name}</b>. "
                         "This is your #1 revenue blocker."),
                "action": f"&#128073; Fix: A/B test the {step_name} page. "
                          "Reduce friction (fewer form fields, add trust signals, faster load time). "
                          "A 10% improvement here compounds through the entire funnel."
            })

    # ── Actions Summary ──
    actions = [i["action"] for i in insights if i["type"] in ("critical", "warning")]

    return insights, actions


# ══════════════════════════════════════════════
# CUSTOMER SEGMENTATION (RFM)
# ══════════════════════════════════════════════
def _safe_qcut(series: pd.Series, n_bins: int, ascending: bool = True) -> pd.Series:
    """
    Robust quantile-cut that handles:
      - Fewer unique values than requested bins  → reduces bin count
      - Single unique value                      → everyone scores 2 (neutral)
      - Any remaining ValueError                 → rank-based fallback scored 1-4
    Always returns a float Series on a 1-4 scale.
    """
    n_unique = series.nunique()
    bins     = min(n_bins, n_unique)

    if bins < 2:
        return pd.Series(2.0, index=series.index)

    raw_labels = list(range(1, bins + 1))
    if not ascending:
        raw_labels = raw_labels[::-1]

    try:
        cut = pd.qcut(series, bins, labels=raw_labels, duplicates="drop").astype(float)
    except ValueError:
        # Rank-based fallback: normalise rank to 1-4 range
        ranked = series.rank(method="first", pct=True)
        cut    = (ranked * 3 + 1).clip(1, 4)
        if not ascending:
            cut = 5 - cut
        return cut.fillna(2.0)

    # Re-scale reduced bins back to 1-4 so all three RFM axes are comparable
    if bins < n_bins:
        lo, hi = cut.min(), cut.max()
        if hi > lo:
            cut = (cut - lo) / (hi - lo) * 3 + 1
        else:
            cut = pd.Series(2.0, index=series.index)

    return cut.fillna(cut.median())


@st.cache_data
def compute_rfm(data_hash, _df):
    if _df.empty or "Customer ID" not in _df.columns:
        return pd.DataFrame()

    snapshot = _df["InvoiceDate"].max() + timedelta(days=1)
    rfm = _df.groupby("Customer ID").agg(
        Recency   = ("InvoiceDate", lambda x: (snapshot - x.max()).days),
        Frequency = ("month",       "nunique"),
        Monetary  = ("Revenue",     "sum"),
    ).reset_index()

    # R: lower recency (more recent) = higher score  →  ascending=False
    rfm["R"] = _safe_qcut(rfm["Recency"],   4, ascending=False)
    # F & M: higher values = higher score            →  ascending=True
    rfm["F"] = _safe_qcut(rfm["Frequency"], 4, ascending=True)
    rfm["M"] = _safe_qcut(rfm["Monetary"],  4, ascending=True)

    rfm["Score"] = rfm[["R", "F", "M"]].mean(axis=1)

    def segment(row):
        if row["Score"] >= 3.5: return "Champions"
        if row["Score"] >= 2.5: return "Loyal"
        if row["Score"] >= 1.5: return "At Risk"
        return "Lost"

    rfm["Segment"] = rfm.apply(segment, axis=1)
    return rfm


# ══════════════════════════════════════════════
# ANOMALY DETECTION
# ══════════════════════════════════════════════
@st.cache_data
def detect_anomalies(data_hash, _daily_rev):
    if len(_daily_rev) < 7:
        return pd.DataFrame()
    mean = _daily_rev["Revenue"].mean()
    std  = _daily_rev["Revenue"].std()
    anom = _daily_rev[
        (_daily_rev["Revenue"] > mean + 2*std) |
        (_daily_rev["Revenue"] < mean - 2*std)
    ].copy()
    anom["z_score"] = (anom["Revenue"] - mean) / std
    anom["type"]    = anom["z_score"].apply(lambda z: "spike" if z > 0 else "drop")
    return anom.sort_values("z_score", key=abs, ascending=False).head(8)


# ══════════════════════════════════════════════
# SMART Q&A ENGINE (pure Python, no external API)
# ══════════════════════════════════════════════
def answer_business_question(question: str, _df, _rfm, _monthly_rev,
                              _growth, _arpu, _repeat_rate, _aov,
                              _total_rev, _total_users, _funnel) -> str:
    q = question.lower().strip()

    # ── Why did sales drop? ──
    if any(x in q for x in ["sales drop", "revenue drop", "drop", "decline", "fell", "down"]):
        if len(_monthly_rev) < 2:
            return "Not enough monthly data to identify a sales drop."
        rev_vals = _monthly_rev["Revenue"].values
        drops    = []
        for i in range(1, len(rev_vals)):
            if rev_vals[i-1] > 0:
                chg = (rev_vals[i] - rev_vals[i-1]) / rev_vals[i-1] * 100
                if chg < -5:
                    drops.append((_monthly_rev.iloc[i]["month"], chg))
        if not drops:
            return (f"<b>Good news: No significant sales drops detected.</b><br><br>"
                    f"Revenue grew <b>{_growth:+.1f}%</b> overall. "
                    f"The trend is positive. Keep monitoring MoM changes for early warning signals.")
        worst = min(drops, key=lambda x: x[1])
        country_rev = _df.groupby("Country")["Revenue"].sum().sort_values(ascending=False)
        top_c = country_rev.index[0] if not country_rev.empty else "N/A"
        return (
            f"<b>Sales Drop Analysis:</b><br><br>"
            f"Found <b>{len(drops)}</b> month(s) with >5% revenue decline.<br>"
            f"Worst drop: <b>{worst[0]}</b> at <b>{worst[1]:.1f}%</b><br><br>"
            f"<b>Likely Causes:</b><br>"
            f"&#8226; Seasonal demand shift — check if {worst[0]} is historically low<br>"
            f"&#8226; Customer churn — repeat rate is <b>{_repeat_rate:.1f}%</b>"
            + (" (critically low)" if _repeat_rate < 30 else "") + "<br>"
            f"&#8226; Geographic dependency — <b>{top_c}</b> drives the most revenue; "
            f"a dip there cascades to total<br><br>"
            f"<b>Action Plan:</b><br>"
            f"1. Run win-back emails to customers who haven't ordered in 60+ days<br>"
            f"2. Analyse top-selling SKUs — were they out of stock during the drop?<br>"
            f"3. Check if new competition entered the market in {worst[0]}"
        )

    # ── How to increase customer retention? ──
    elif any(x in q for x in ["retention", "churn", "keep customers", "repeat", "loyalty"]):
        lost_pct  = 100 - _repeat_rate
        rev_at_risk = _total_rev * (lost_pct / 100) * 0.3
        return (
            f"<b>Customer Retention Analysis:</b><br><br>"
            f"Current repeat purchase rate: <b>{_repeat_rate:.1f}%</b><br>"
            f"Estimated revenue at risk from churn: <b>${rev_at_risk:,.0f}/yr</b><br><br>"
            f"<b>Top Retention Strategies (ranked by impact):</b><br><br>"
            f"<b>1. Post-Purchase Email Sequence (highest ROI)</b><br>"
            f"&nbsp;&nbsp;Day 3: 'How are you enjoying your purchase?'<br>"
            f"&nbsp;&nbsp;Day 7: Related product recommendation<br>"
            f"&nbsp;&nbsp;Day 14: 10% off next order<br><br>"
            f"<b>2. Loyalty Programme</b><br>"
            f"&nbsp;&nbsp;Points per purchase, redeemable for discounts<br>"
            f"&nbsp;&nbsp;Expected impact: +15-25% repeat rate<br><br>"
            f"<b>3. Personalised Recommendations</b><br>"
            f"&nbsp;&nbsp;'Customers like you also bought...' increases basket size by ~20%<br><br>"
            f"<b>4. Win-Back Campaign</b><br>"
            f"&nbsp;&nbsp;Target customers inactive 60+ days with a compelling offer<br>"
            f"&nbsp;&nbsp;Aim for 10-20% reactivation rate<br><br>"
            f"<b>Target:</b> Get repeat rate from {_repeat_rate:.0f}% to 50%+ in 6 months"
        )

    # ── Which users bring most profit? ──
    elif any(x in q for x in ["most profit", "best customers", "top customers",
                               "high value", "vip", "champions", "80/20"]):
        if _rfm is None or _rfm.empty:
            return "RFM analysis not available for current data selection."
        champs = _rfm[_rfm["Segment"] == "Champions"]
        total_cust   = len(_rfm)
        champ_count  = len(champs)
        champ_rev    = champs["Monetary"].sum()
        champ_pct    = champ_count / total_cust * 100 if total_cust > 0 else 0
        champ_rev_pct= champ_rev / _rfm["Monetary"].sum() * 100 if _rfm["Monetary"].sum() > 0 else 0
        avg_champ_val = champs["Monetary"].mean() if len(champs) > 0 else 0
        return (
            f"<b>High-Value Customer Analysis (RFM Model):</b><br><br>"
            f"<b>Champions Segment:</b><br>"
            f"&#8226; <b>{champ_count:,}</b> customers ({champ_pct:.1f}% of base)<br>"
            f"&#8226; Generate <b>${champ_rev:,.0f}</b> = <b>{champ_rev_pct:.0f}%</b> of total revenue<br>"
            f"&#8226; Average spend per champion: <b>${avg_champ_val:,.2f}</b><br><br>"
            f"<b>What makes them Champions:</b><br>"
            f"&#8226; Buy recently, buy often, spend the most<br>"
            f"&#8226; High Recency + Frequency + Monetary scores<br><br>"
            f"<b>How to leverage them:</b><br>"
            f"1. <b>Clone them</b> — use their profile for lookalike ad targeting<br>"
            f"2. <b>VIP treatment</b> — early access, exclusive offers, personal thank-you<br>"
            f"3. <b>Referral programme</b> — they love your brand; make them ambassadors<br>"
            f"4. <b>Survey them</b> — ask why they buy; use answers in marketing copy<br><br>"
            f"<b>Warning:</b> Don't discount to Champions — they already love you. "
            f"Discounts train them to wait for sales."
        )

    # ── Best selling products ──
    elif any(x in q for x in ["product", "sku", "best selling", "top product", "inventory"]):
        if "Description" not in _df.columns:
            return "Product data not available."
        top_p = (_df.groupby("Description")
                 .agg(Revenue=("Revenue","sum"), Orders=("Revenue","count"))
                 .sort_values("Revenue", ascending=False).head(5))
        rows = "".join([
            f"<br><b>{i+1}. {row.name}</b> — ${row['Revenue']:,.0f} revenue, {int(row['Orders']):,} orders"
            for i, (_, row) in enumerate(top_p.iterrows())
        ])
        return (
            f"<b>Top 5 Products by Revenue:</b>{rows}<br><br>"
            f"<b>Action:</b><br>"
            f"1. Ensure top products are never out of stock (set reorder triggers)<br>"
            f"2. Bundle #1 with lower-selling complementary items<br>"
            f"3. Feature top products prominently on homepage and in emails<br>"
            f"4. Analyse margin — high revenue ≠ high profit. Rank by gross margin too."
        )

    # ── Growth strategies ──
    elif any(x in q for x in ["grow", "growth", "increase revenue", "scale",
                               "improve", "strategy", "how to"]):
        return (
            f"<b>Growth Strategy Roadmap:</b><br><br>"
            f"<b>Quick Wins (0-30 days):</b><br>"
            f"&#8226; Email win-back to churned customers — 10% response = significant revenue<br>"
            f"&#8226; Add product bundles — increases AOV from <b>${_aov:,.2f}</b> by 20-40%<br>"
            f"&#8226; Optimise checkout — remove friction to improve funnel conversion<br><br>"
            f"<b>Medium Term (30-90 days):</b><br>"
            f"&#8226; Loyalty programme to improve {_repeat_rate:.0f}% repeat rate<br>"
            f"&#8226; Expand to underperforming countries with localised campaigns<br>"
            f"&#8226; A/B test pricing — test 5-10% price increase on top SKUs<br><br>"
            f"<b>Long Term (90+ days):</b><br>"
            f"&#8226; Subscription offering — converts one-time buyers to recurring revenue<br>"
            f"&#8226; Private label products — higher margins on proven sellers<br>"
            f"&#8226; B2B channel — wholesale to businesses (typically 3-5x order sizes)<br><br>"
            f"<b>Key Metric to Watch:</b> LTV:CAC ratio. "
            f"Aim for >3:1. Currently estimating LTV ~${_arpu * 3:,.0f} based on ARPU."
        )

    # ── Seasonal patterns ──
    elif any(x in q for x in ["season", "peak", "holiday", "when", "best month", "worst month"]):
        if _monthly_rev.empty:
            return "Not enough data for seasonal analysis."
        best  = _monthly_rev.loc[_monthly_rev["Revenue"].idxmax()]
        worst = _monthly_rev.loc[_monthly_rev["Revenue"].idxmin()]
        return (
            f"<b>Seasonality Analysis:</b><br><br>"
            f"&#8226; <b>Peak month:</b> {best['month']} — ${best['Revenue']:,.0f}<br>"
            f"&#8226; <b>Slowest month:</b> {worst['month']} — ${worst['Revenue']:,.0f}<br>"
            f"&#8226; <b>Revenue range:</b> ${worst['Revenue']:,.0f} to ${best['Revenue']:,.0f} "
            f"({best['Revenue']/worst['Revenue']:.1f}x swing)<br><br>"
            f"<b>Strategic Recommendations:</b><br>"
            f"1. <b>Pre-peak:</b> Build inventory and launch campaigns 6-8 weeks before {best['month']}<br>"
            f"2. <b>Peak month:</b> Maximise ad spend — highest conversion period<br>"
            f"3. <b>Off-peak ({worst['month']}):</b> Run clearance sales, develop new products, "
            f"invest in brand building<br>"
            f"4. <b>Smooth revenue:</b> Introduce subscription products to reduce seasonality impact"
        )

    # ── Default intelligent response ──
    else:
        return (
            f"<b>Business Intelligence Summary:</b><br><br>"
            f"I can answer questions like:<br>"
            f"&#8226; 'Why did sales drop?'<br>"
            f"&#8226; 'How to increase customer retention?'<br>"
            f"&#8226; 'Which users bring most profit?'<br>"
            f"&#8226; 'What are my best selling products?'<br>"
            f"&#8226; 'How can I grow revenue?'<br>"
            f"&#8226; 'What are the seasonal patterns?'<br><br>"
            f"<b>Current Snapshot:</b><br>"
            f"Revenue: <b>${_total_rev:,.0f}</b> | Users: <b>{_total_users:,}</b> | "
            f"ARPU: <b>${_arpu:.2f}</b> | Repeat Rate: <b>{_repeat_rate:.1f}%</b>"
        )


# ══════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════
st.markdown(f"""
<div class='dash-header'>
  <div style='display:flex;align-items:center;flex-wrap:wrap;gap:8px;'>
    <span class='dash-title'>Startup Intelligence</span>
    <span class='live-pill'>Live</span>
  </div>
  <div class='dash-sub'>AI-Powered Business Analytics &middot; {mode} Mode &middot; USD $</div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# KPI ROW (always visible)
# ══════════════════════════════════════════════
KPIS = [
    dict(icon="👥", lbl="Total Users",     val=f"{total_users:,}",
         delta=f"{'↗' if growth>=0 else '↘'} {abs(growth):.1f}% growth",
         dc="up" if growth>=0 else "dn",
         grad="linear-gradient(90deg,#63B3ED,#4FD1C5)", gc="#63B3ED"),
    dict(icon="🛒", lbl="Total Orders",    val=f"{total_orders:,}",
         delta="Transactions",              dc="nt",
         grad="linear-gradient(90deg,#B794F4,#63B3ED)", gc="#B794F4"),
    dict(icon="💰", lbl="Total Revenue",   val=f"${total_revenue:,.0f}",
         delta="USD",                       dc="nt",
         grad="linear-gradient(90deg,#68D391,#4FD1C5)", gc="#68D391"),
    dict(icon="📊", lbl="ARPU",            val=f"${arpu:,.2f}",
         delta="Per User",
         dc="up" if arpu>=100 else ("nt" if arpu>=50 else "dn"),
         grad="linear-gradient(90deg,#F6AD55,#FC8181)", gc="#F6AD55"),
    dict(icon="🔄", lbl="Repeat Rate",     val=f"{repeat_rate:.1f}%",
         delta="Returning Buyers",
         dc="up" if repeat_rate>=50 else ("nt" if repeat_rate>=30 else "dn"),
         grad="linear-gradient(90deg,#4FD1C5,#B794F4)", gc="#4FD1C5"),
    dict(icon="🧾", lbl="Avg Order Value", val=f"${aov:,.2f}",
         delta=f"MoM {mom_change:+.1f}%",
         dc="up" if mom_change>=0 else "dn",
         grad="linear-gradient(90deg,#68D391,#F6AD55)", gc="#68D391"),
]

kpi_cols = st.columns(6)
for col, k in zip(kpi_cols, KPIS):
    with col:
        st.markdown(f"""
<div class='kpi-wrap' style='--kpi-grad:{k["grad"]};--kpi-gc:{k["gc"]};'>
  <div class='kpi-orb'></div>
  <span class='kpi-icon'>{k["icon"]}</span>
  <div class='kpi-lbl'>{k["lbl"]}</div>
  <div class='kpi-val'>{k["val"]}</div>
  <div class='kpi-delta {k["dc"]}'>{k["delta"]}</div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# RFM + AI ANALYSIS (computed once, used in tabs)
# ══════════════════════════════════════════════
rfm          = compute_rfm(str(df.shape), df)
daily_rev    = df.groupby("day")["Revenue"].sum().reset_index()
anomalies    = detect_anomalies(str(df.shape), daily_rev)
ai_insights, ai_actions = run_ai_analysis(
    str(df.shape), df, monthly_rev, funnel,
    growth, arpu, repeat_rate, mom_change
)


# ══════════════════════════════════════════════
# TAB LAYOUT
# ══════════════════════════════════════════════
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "🧠 AI Analyst",
    "👥 Customers",
    "📉 Sales Diagnostics",
    "🚀 Growth Ops",
])


# ─────────────────────────────────────────────
# TAB 1 — OVERVIEW
# ─────────────────────────────────────────────
with tab1:
    sec("📈 Revenue & Activity Trends")

    c1, c2 = st.columns(2)
    with c1:
        fig = go.Figure(go.Bar(
            x=monthly_rev["month"], y=monthly_rev["Revenue"],
            marker=dict(color=monthly_rev["Revenue"],
                        colorscale=[[0,"rgba(99,179,237,0.3)"],[1,"#63B3ED"]],
                        line=dict(width=0)),
            hovertemplate="<b>%{x}</b><br>$%{y:,.0f}<extra></extra>",
        ))
        T(fig, "Monthly Revenue ($)")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

    with c2:
        dau = df.groupby("day")["Customer ID"].nunique().reset_index()
        fig = go.Figure(go.Scatter(
            x=dau["day"], y=dau["Customer ID"],
            mode="lines", fill="tozeroy",
            line=dict(color="#4FD1C5", width=2),
            fillcolor="rgba(79,209,197,0.07)",
            hovertemplate="<b>%{x}</b><br>Users: %{y}<extra></extra>",
        ))
        T(fig, "Daily Active Users")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

    c3, c4 = st.columns([3, 2])
    with c3:
        sec("🏆 Top Products vs Top Countries")
        p_col, c_col = st.columns(2)
        with p_col:
            tp = (df.groupby("Description")["Quantity"].sum()
                  .nlargest(8).reset_index().sort_values("Quantity"))
            fig = go.Figure(go.Bar(
                x=tp["Quantity"], y=tp["Description"], orientation="h",
                marker=dict(color=tp["Quantity"],
                            colorscale=[[0,"rgba(183,148,244,0.3)"],[1,"#B794F4"]],
                            line=dict(width=0)),
                hovertemplate="<b>%{y}</b><br>%{x:,} units<extra></extra>",
            ))
            T(fig, "Top Products")
            fig.update_layout(yaxis=dict(tickfont=dict(size=9), automargin=True))
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

        with c_col:
            tc = (df.groupby("Country")["Revenue"].sum()
                  .nlargest(8).reset_index().sort_values("Revenue"))
            fig = go.Figure(go.Bar(
                x=tc["Revenue"], y=tc["Country"], orientation="h",
                marker=dict(color=tc["Revenue"],
                            colorscale=[[0,"rgba(104,211,145,0.3)"],[1,"#68D391"]],
                            line=dict(width=0)),
                hovertemplate="<b>%{y}</b><br>$%{x:,.0f}<extra></extra>",
            ))
            T(fig, "Top Countries")
            fig.update_layout(yaxis=dict(tickfont=dict(size=9), automargin=True))
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

    with c4:
        sec("🔄 Conversion Funnel")
        n   = len(funnel)
        fig = go.Figure(go.Funnel(
            y=funnel["Step"], x=funnel["Count"],
            marker=dict(color=PAL[:n], line=dict(width=0)),
            textinfo="value+percent initial",
            textfont=dict(color="#EDF2F7", size=11),
            connector=dict(line=dict(color="rgba(99,179,237,0.15)", width=2)),
        ))
        T(fig, "Conversion Funnel")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

    # Heatmap: Orders by day-of-week x hour
    sec("⏰ When Do Customers Buy? (Day × Hour Heatmap)")
    try:
        heat_data = df.groupby(["dow","hour"]).size().reset_index(name="orders")
        day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        heat_data["dow"] = pd.Categorical(heat_data["dow"], categories=day_order, ordered=True)
        heat_pivot = heat_data.pivot(index="dow", columns="hour", values="orders").fillna(0)
        fig_h = px.imshow(heat_pivot, aspect="auto",
                          color_continuous_scale=[[0,"#060F1E"],[0.4,"#1A365D"],[1,"#63B3ED"]],
                          title="Order Volume by Day & Hour")
        T(fig_h)
        fig_h.update_layout(coloraxis_colorbar=dict(
            title="Orders", tickfont=dict(color="#718096")))
        st.plotly_chart(fig_h, use_container_width=True, config={"displayModeBar":False})
    except Exception as e:
        st.info(f"Day/Hour heatmap unavailable: {e}")


# ─────────────────────────────────────────────
# TAB 2 — AI ANALYST
# ─────────────────────────────────────────────
with tab2:
    sec("🧠 AI Business Intelligence", badge="AUTO-GENERATED", badge_color="#B794F4")

    # Insight cards
    if ai_insights:
        left_col, right_col = st.columns(2)
        for i, ins in enumerate(ai_insights):
            target = left_col if i % 2 == 0 else right_col
            with target:
                st.markdown(f"""
<div class='ai-card {ins["type"]}'>
  <div class='ai-card-badge'>{ins["type"].upper()}</div>
  <div class='ai-card-title'>{ins["title"]}</div>
  <div class='ai-card-body'>{ins["body"]}</div>
  <div class='ai-card-action'>{ins["action"]}</div>
</div>""", unsafe_allow_html=True)

    # ── Anomaly Detection ──
    sec("⚡ Revenue Anomalies Detected", badge=f"{len(anomalies)} FOUND",
        badge_color="#F6AD55" if len(anomalies) > 0 else "#68D391")

    if not anomalies.empty:
        a1, a2 = st.columns([2, 1])
        with a1:
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=daily_rev["day"], y=daily_rev["Revenue"],
                mode="lines", name="Revenue",
                line=dict(color="rgba(99,179,237,0.5)", width=1.5),
                hovertemplate="%{x}<br>$%{y:,.0f}<extra></extra>",
            ))
            mean_r = daily_rev["Revenue"].mean()
            std_r  = daily_rev["Revenue"].std()
            fig.add_hline(y=mean_r + 2*std_r, line_dash="dot",
                          line_color="rgba(246,173,85,0.4)", annotation_text="+2σ")
            fig.add_hline(y=mean_r - 2*std_r, line_dash="dot",
                          line_color="rgba(252,129,129,0.4)", annotation_text="-2σ")
            fig.add_trace(go.Scatter(
                x=anomalies["day"], y=anomalies["Revenue"],
                mode="markers", name="Anomalies",
                marker=dict(
                    color=anomalies["type"].map({"spike":"#F6AD55","drop":"#FC8181"}),
                    size=10, symbol="diamond",
                    line=dict(width=2, color="#EDF2F7")
                ),
                hovertemplate="<b>%{x}</b><br>$%{y:,.0f} ⚡<extra></extra>",
            ))
            T(fig, "Revenue with Anomaly Detection")
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

        with a2:
            st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)
            for _, row in anomalies.iterrows():
                color = "#F6AD55" if row["type"] == "spike" else "#FC8181"
                icon  = "⬆" if row["type"] == "spike" else "⬇"
                st.markdown(f"""
<div class='anomaly-row'>
  <span style='color:{color};font-size:1.1rem;'>{icon}</span>
  <div>
    <div style='color:#EDF2F7;font-size:.8rem;font-weight:600;'>{row['day']}</div>
    <div style='color:{color};font-size:.75rem;'>${row['Revenue']:,.0f}
      &nbsp;·&nbsp; z={row['z_score']:+.1f}σ</div>
  </div>
</div>""", unsafe_allow_html=True)
    else:
        st.success("✅ No revenue anomalies detected in the selected period.")

    # ── Interactive Q&A ──
    sec("💬 Ask the AI Analyst", badge="BUSINESS Q&A", badge_color="#63B3ED")

    preset_questions = [
        "Why did sales drop?",
        "How to increase customer retention?",
        "Which users bring most profit?",
        "What are my best selling products?",
        "How can I grow revenue?",
        "What are the seasonal patterns?",
    ]

    st.markdown("<div style='margin-bottom:.5rem;font-size:.75rem;color:#4A5568;"
                "font-weight:600;text-transform:uppercase;letter-spacing:.1em;'>"
                "Quick Questions</div>", unsafe_allow_html=True)

    q_cols = st.columns(3)
    for i, pq in enumerate(preset_questions):
        with q_cols[i % 3]:
            if st.button(pq, key=f"pq_{i}"):
                st.session_state["qa_question"] = pq

    st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)
    custom_q = st.text_input(
        "Or type your own business question...",
        value=st.session_state.get("qa_question", ""),
        placeholder="e.g. Why did November revenue spike?",
        key="qa_input",
    )

    if custom_q:
        answer = answer_business_question(
            custom_q, df, rfm, monthly_rev,
            growth, arpu, repeat_rate, aov,
            total_revenue, total_users, funnel
        )
        st.markdown(f"""
<div class='qa-answer'>
  <div style='font-family:Space Mono,monospace;font-size:.62rem;color:#4A5568;
              letter-spacing:.1em;text-transform:uppercase;margin-bottom:.6rem;'>
    &#129302; AI Analyst Response
  </div>
  {answer}
</div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# TAB 3 — CUSTOMER INTELLIGENCE
# ─────────────────────────────────────────────
with tab3:
    sec("👥 Customer Segmentation (RFM Model)",
        badge="RECENCY · FREQUENCY · MONETARY", badge_color="#4FD1C5")

    if not rfm.empty:
        seg_counts = rfm["Segment"].value_counts()
        seg_rev    = rfm.groupby("Segment")["Monetary"].sum()
        seg_colors = {"Champions":"#68D391","Loyal":"#63B3ED",
                      "At Risk":"#F6AD55","Lost":"#FC8181"}

        # Segment summary cards
        sc1, sc2, sc3, sc4 = st.columns(4)
        for col, seg in zip([sc1,sc2,sc3,sc4], ["Champions","Loyal","At Risk","Lost"]):
            count = seg_counts.get(seg, 0)
            rev   = seg_rev.get(seg, 0)
            pct   = count / len(rfm) * 100 if len(rfm) > 0 else 0
            color = seg_colors[seg]
            with col:
                st.markdown(f"""
<div class='seg-card' style='border-top:3px solid {color};'>
  <div class='seg-val' style='color:{color};'>{count:,}</div>
  <div class='seg-lbl'>{seg}</div>
  <div class='seg-pct' style='color:{color};'>{pct:.1f}% of base</div>
  <div style='font-size:.72rem;color:#4A5568;margin-top:.3rem;'>${rev:,.0f} revenue</div>
</div>""", unsafe_allow_html=True)

        st.markdown("<div style='height:1.5rem;'></div>", unsafe_allow_html=True)

        r1, r2 = st.columns(2)
        with r1:
            fig = px.scatter(
                rfm, x="Recency", y="Monetary", color="Segment",
                size="Frequency", size_max=18,
                color_discrete_map=seg_colors,
                hover_data=["Customer ID","Frequency"],
                title="RFM Scatter: Recency vs Revenue",
                labels={"Recency":"Days Since Last Purchase","Monetary":"Total Revenue ($)"},
            )
            T(fig)
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

        with r2:
            seg_df = rfm.groupby("Segment").agg(
                Count=("Customer ID","count"),
                Revenue=("Monetary","sum"),
                Avg_Revenue=("Monetary","mean"),
            ).reset_index()
            fig = go.Figure(go.Treemap(
                labels=seg_df["Segment"],
                values=seg_df["Revenue"],
                parents=[""] * len(seg_df),
                marker_colors=[seg_colors.get(s,"#63B3ED") for s in seg_df["Segment"]],
                textinfo="label+value+percent root",
                textfont=dict(size=13, color="#EDF2F7"),
                hovertemplate="<b>%{label}</b><br>Revenue: $%{value:,.0f}<br>%{percentRoot}<extra></extra>",
            ))
            T(fig, "Revenue Share by Segment")
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

        # Top customers table
        sec("💎 Top 15 Most Valuable Customers")
        top_custs = rfm.sort_values("Monetary", ascending=False).head(15)
        table_rows = ""
        for i, (_, row) in enumerate(top_custs.iterrows()):
            color = seg_colors.get(row["Segment"], "#63B3ED")
            table_rows += (
                f"<tr style='border-bottom:1px solid rgba(255,255,255,0.04);'>"
                f"<td style='padding:.55rem .5rem;color:#718096;font-family:Space Mono,monospace;"
                f"font-size:.72rem;'>#{i+1}</td>"
                f"<td style='padding:.55rem .5rem;color:#EDF2F7;font-family:Space Mono,monospace;"
                f"font-size:.78rem;'>{int(row['Customer ID'])}</td>"
                f"<td style='padding:.55rem .5rem;color:#68D391;font-family:Space Mono,monospace;"
                f"font-size:.82rem;font-weight:700;'>${row['Monetary']:,.2f}</td>"
                f"<td style='padding:.55rem .5rem;color:#A0AEC0;font-size:.78rem;'>{int(row['Frequency'])}x</td>"
                f"<td style='padding:.55rem .5rem;color:#718096;font-size:.78rem;'>{int(row['Recency'])}d ago</td>"
                f"<td style='padding:.55rem .5rem;'>"
                f"<span style='background:rgba(0,0,0,.3);color:{color};font-size:.62rem;"
                f"font-weight:700;padding:2px 8px;border-radius:8px;border:1px solid {color}44;'>"
                f"{row['Segment']}</span></td>"
                f"</tr>"
            )
        st.markdown(f"""
<div style='background:rgba(11,21,37,.9);border:1px solid rgba(99,179,237,.12);
            border-radius:14px;padding:1.2rem;overflow-x:auto;'>
  <table style='width:100%;border-collapse:collapse;font-size:.84rem;'>
    <thead><tr style='border-bottom:1px solid rgba(99,179,237,0.15);'>
      <th style='padding:.5rem;color:#4A5568;font-size:.62rem;letter-spacing:.1em;
                 text-transform:uppercase;text-align:left;'>#</th>
      <th style='padding:.5rem;color:#4A5568;font-size:.62rem;letter-spacing:.1em;
                 text-transform:uppercase;text-align:left;'>Customer ID</th>
      <th style='padding:.5rem;color:#4A5568;font-size:.62rem;letter-spacing:.1em;
                 text-transform:uppercase;text-align:left;'>Total Revenue</th>
      <th style='padding:.5rem;color:#4A5568;font-size:.62rem;letter-spacing:.1em;
                 text-transform:uppercase;text-align:left;'>Orders</th>
      <th style='padding:.5rem;color:#4A5568;font-size:.62rem;letter-spacing:.1em;
                 text-transform:uppercase;text-align:left;'>Last Purchase</th>
      <th style='padding:.5rem;color:#4A5568;font-size:.62rem;letter-spacing:.1em;
                 text-transform:uppercase;text-align:left;'>Segment</th>
    </tr></thead>
    <tbody>{table_rows}</tbody>
  </table>
</div>""", unsafe_allow_html=True)

    else:
        st.info("Customer segmentation requires Customer ID data in current selection.")

    # Retention cohort
    sec("🔥 Retention Cohort Heatmap")
    try:
        cust_weeks  = df.groupby("Customer ID")["week"].nunique()
        active_cust = cust_weeks[cust_weeks >= 2].index
        df_coh      = df[df["Customer ID"].isin(active_cust)].copy()
        cohort      = (df_coh.groupby(["Customer ID","week"]).size()
                       .reset_index(name="activity"))
        pivot       = cohort.pivot_table(index="Customer ID", columns="week",
                                         values="activity", fill_value=0)
        _map_fn     = pivot.map if hasattr(pivot,"map") else pivot.applymap
        binary      = _map_fn(lambda x: 1 if x > 0 else 0)
        first_col   = binary.iloc[:,0].replace(0, np.nan)
        retention   = binary.divide(first_col, axis=0).fillna(0)
        if retention.shape[0] > 250:
            retention = retention.sample(250, random_state=42)
        fig_h = px.imshow(retention, aspect="auto",
                          color_continuous_scale=[[0,"#060F1E"],[0.4,"#1A365D"],[1,"#63B3ED"]],
                          title="User Retention by Week", zmin=0, zmax=1)
        T(fig_h)
        fig_h.update_layout(coloraxis_colorbar=dict(
            title="Rate", tickformat=".0%", tickfont=dict(color="#718096")))
        st.plotly_chart(fig_h, use_container_width=True, config={"displayModeBar":False})
    except Exception as e:
        st.warning(f"Retention heatmap skipped: {e}")


# ─────────────────────────────────────────────
# TAB 4 — SALES DIAGNOSTICS
# ─────────────────────────────────────────────
with tab4:
    sec("📉 Sales Drop Diagnostic", badge="ROOT CAUSE ANALYSIS", badge_color="#FC8181")

    # MoM waterfall
    if len(monthly_rev) >= 2:
        monthly_rev_copy = monthly_rev.copy()
        monthly_rev_copy["MoM_change"] = monthly_rev_copy["Revenue"].diff()
        monthly_rev_copy["MoM_pct"]    = monthly_rev_copy["Revenue"].pct_change() * 100

        fig = go.Figure()
        colors = ["#68D391" if x >= 0 else "#FC8181"
                  for x in monthly_rev_copy["MoM_change"].fillna(0)]
        fig.add_trace(go.Bar(
            x=monthly_rev_copy["month"],
            y=monthly_rev_copy["MoM_change"].fillna(0),
            marker_color=colors,
            hovertemplate="<b>%{x}</b><br>Change: $%{y:,.0f}<extra></extra>",
            name="MoM Change",
        ))
        fig.add_hline(y=0, line_color="rgba(255,255,255,0.2)", line_width=1)
        T(fig, "Month-over-Month Revenue Change ($)")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

    # Country performance vs average
    sec("🌍 Country Performance vs Benchmark")
    country_stats = df.groupby("Country").agg(
        Revenue=("Revenue","sum"),
        Orders=("Revenue","count"),
        Customers=("Customer ID","nunique"),
    ).reset_index()
    country_stats["ARPU"] = country_stats["Revenue"] / country_stats["Customers"]
    avg_arpu = country_stats["ARPU"].mean()
    country_stats["vs_avg"] = country_stats["ARPU"] - avg_arpu
    country_stats["status"] = country_stats["vs_avg"].apply(
        lambda x: "Above Average" if x > 0 else "Below Average")
    top_c = country_stats.nlargest(15, "Revenue")

    fig = go.Figure(go.Bar(
        x=top_c["Country"],
        y=top_c["vs_avg"],
        marker_color=top_c["status"].map(
            {"Above Average":"#68D391", "Below Average":"#FC8181"}),
        hovertemplate="<b>%{x}</b><br>ARPU vs avg: $%{y:+.2f}<extra></extra>",
    ))
    fig.add_hline(y=0, line_color="rgba(255,255,255,0.3)", line_width=1,
                  annotation_text=f"Avg ARPU ${avg_arpu:.2f}")
    T(fig, "Country ARPU vs Average Benchmark")
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

    # Product velocity analysis
    sec("📦 Product Velocity & Revenue Contribution")
    try:
        prod_stats = df.groupby("Description").agg(
            Revenue=("Revenue","sum"),
            Quantity=("Quantity","sum"),
            Orders=("Revenue","count"),
        ).reset_index()
        prod_stats["Rev_pct"] = prod_stats["Revenue"] / prod_stats["Revenue"].sum() * 100
        prod_stats["cumulative"] = prod_stats.sort_values("Revenue", ascending=False)["Rev_pct"].cumsum()

        top_prod = prod_stats.nlargest(20, "Revenue")
        fig = px.scatter(
            top_prod, x="Quantity", y="Revenue",
            size="Orders", color="Revenue",
            color_continuous_scale=[[0,"rgba(99,179,237,0.3)"],[1,"#63B3ED"]],
            hover_name="Description",
            title="Product: Volume vs Revenue (bubble = order count)",
            labels={"Quantity":"Units Sold","Revenue":"Total Revenue ($)"},
        )
        T(fig)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})
    except Exception as e:
        st.info(f"Product velocity chart unavailable: {e}")

    # Funnel drop analysis
    sec("🔄 Funnel Drop-Off Analysis")
    if len(funnel) >= 2:
        fd = funnel.copy().reset_index(drop=True)
        fd["Conv %"]  = (fd["Count"] / fd["Count"].iloc[0] * 100).round(1)
        fd["Drop %"]  = -(fd["Count"].pct_change() * 100).round(1)
        fd["Drop %"]  = fd["Drop %"].fillna(0)

        f1, f2 = st.columns([1,2])
        with f1:
            fig = go.Figure(go.Funnel(
                y=fd["Step"], x=fd["Count"],
                marker=dict(color=PAL[:len(fd)], line=dict(width=0)),
                textinfo="value+percent initial",
                textfont=dict(color="#EDF2F7", size=12),
                connector=dict(line=dict(color="rgba(99,179,237,0.15)", width=2)),
            ))
            T(fig, "Conversion Funnel")
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

        with f2:
            rows = ""
            for i, row in fd.iterrows():
                c    = PAL[i % len(PAL)]
                drop = row["Drop %"]
                sev  = "critical" if drop > 50 else ("warning" if drop > 25 else "positive")
                sev_color = {"critical":"#FC8181","warning":"#F6AD55","positive":"#68D391"}[sev]
                rows += (
                    f"<tr style='border-bottom:1px solid rgba(255,255,255,0.04);'>"
                    f"<td style='padding:.6rem .5rem;color:#EDF2F7;'>"
                    f"<span style='width:8px;height:8px;display:inline-block;"
                    f"border-radius:50%;background:{c};margin-right:8px;'></span>"
                    f"{row['Step']}</td>"
                    f"<td style='text-align:right;padding:.6rem .5rem;color:#A0AEC0;"
                    f"font-family:Space Mono,monospace;'>{int(row['Count']):,}</td>"
                    f"<td style='text-align:right;padding:.6rem .5rem;color:{c};"
                    f"font-family:Space Mono,monospace;font-weight:700;'>{row['Conv %']:.1f}%</td>"
                    f"<td style='text-align:right;padding:.6rem .5rem;color:{sev_color};"
                    f"font-family:Space Mono,monospace;'>"
                    f"{'↓'+str(abs(drop))+'%' if drop > 0 else '—'}</td>"
                    f"</tr>"
                )
            st.markdown(f"""
<div style='background:rgba(11,21,37,.9);border:1px solid rgba(99,179,237,.12);
            border-radius:14px;padding:1.2rem;margin-top:.5rem;'>
  <div style='font-family:Space Mono,monospace;font-size:.65rem;color:#4A5568;
              letter-spacing:.1em;text-transform:uppercase;margin-bottom:.8rem;'>
    Funnel Step Analysis
  </div>
  <table style='width:100%;border-collapse:collapse;'>
    <thead><tr style='border-bottom:1px solid rgba(99,179,237,.15);'>
      <th style='text-align:left;padding:.5rem;color:#4A5568;font-size:.6rem;
                 letter-spacing:.1em;text-transform:uppercase;'>Step</th>
      <th style='text-align:right;padding:.5rem;color:#4A5568;font-size:.6rem;
                 letter-spacing:.1em;text-transform:uppercase;'>Count</th>
      <th style='text-align:right;padding:.5rem;color:#4A5568;font-size:.6rem;
                 letter-spacing:.1em;text-transform:uppercase;'>Conv %</th>
      <th style='text-align:right;padding:.5rem;color:#4A5568;font-size:.6rem;
                 letter-spacing:.1em;text-transform:uppercase;'>Drop %</th>
    </tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# TAB 5 — GROWTH OPPORTUNITIES
# ─────────────────────────────────────────────
with tab5:
    sec("🚀 Growth Opportunity Finder", badge="AI STRATEGY", badge_color="#68D391")

    # Priority action cards
    priority_actions = [
        {
            "priority": "P1", "color": "#FC8181",
            "title": "Fix Retention First",
            "effort": "Medium", "impact": "Very High",
            "body": (f"Retention ({repeat_rate:.0f}%) is the single highest-ROI lever. "
                     "Fixing churn delivers revenue without additional acquisition spend."),
            "steps": ["Set up 3-email post-purchase sequence",
                      "Create 10% discount for 2nd purchase",
                      "Build reactivation campaign for 60-day inactive customers"],
        },
        {
            "priority": "P2", "color": "#F6AD55",
            "title": "Increase Average Order Value",
            "effort": "Low", "impact": "High",
            "body": (f"AOV is <b>${aov:,.2f}</b>. Product bundling and minimum spend thresholds "
                     "can increase this by 20-40% with zero new customer acquisition cost."),
            "steps": ["Create 3-5 product bundles from top SKUs",
                      "Add 'You may also like' recommendations",
                      "Set free shipping threshold 20% above current AOV"],
        },
        {
            "priority": "P3", "color": "#68D391",
            "title": "Monetise Champions Segment",
            "effort": "Low", "impact": "High",
            "body": (f"Champions represent your highest-LTV customers. "
                     "They are loyal, low-churn, and the best source of referrals."),
            "steps": ["Launch VIP / loyalty tier for top customers",
                      "Create referral programme (give $10, get $10)",
                      "Survey champions to understand purchase motivation"],
        },
        {
            "priority": "P4", "color": "#63B3ED",
            "title": "Geographic Expansion",
            "effort": "High", "impact": "Medium",
            "body": (f"Only {len(countries)} markets currently active. "
                     "Localising for 2-3 adjacent markets could unlock significant new revenue."),
            "steps": ["Identify top 3 countries with highest order volume but low ARPU",
                      "Translate product descriptions and checkout",
                      "Test localised ad campaigns with $500 budget each"],
        },
    ]

    pr1, pr2 = st.columns(2)
    for i, pa in enumerate(priority_actions):
        col = pr1 if i % 2 == 0 else pr2
        with col:
            steps_html = "".join(
                f"<div style='display:flex;gap:8px;padding:.3rem 0;font-size:.8rem;color:#A0AEC0;'>"
                f"<span style='color:{pa['color']};flex-shrink:0;'>&#10003;</span>{s}</div>"
                for s in pa["steps"]
            )
            st.markdown(f"""
<div style='background:var(--card);border:1px solid {pa["color"]}33;
            border-left:3px solid {pa["color"]};border-radius:14px;
            padding:1.2rem 1.4rem;margin-bottom:.9rem;'>
  <div style='display:flex;align-items:center;gap:10px;margin-bottom:.5rem;'>
    <span style='background:{pa["color"]}22;color:{pa["color"]};font-size:.62rem;
                 font-weight:700;padding:2px 8px;border-radius:6px;
                 letter-spacing:.1em;'>{pa["priority"]}</span>
    <span style='font-size:.95rem;font-weight:700;color:#EDF2F7;'>{pa["title"]}</span>
  </div>
  <div style='display:flex;gap:12px;margin-bottom:.6rem;'>
    <span style='font-size:.68rem;color:#4A5568;'>Effort: <b style='color:#A0AEC0;'>{pa["effort"]}</b></span>
    <span style='font-size:.68rem;color:#4A5568;'>Impact: <b style='color:{pa["color"]};'>{pa["impact"]}</b></span>
  </div>
  <div style='font-size:.83rem;color:#A0AEC0;line-height:1.6;margin-bottom:.7rem;'>{pa["body"]}</div>
  <div style='border-top:1px solid rgba(255,255,255,0.05);padding-top:.6rem;'>{steps_html}</div>
</div>""", unsafe_allow_html=True)

    # Revenue projection
    sec("📈 Revenue Projection (What-If Scenarios)")
    s1, s2, s3 = st.columns(3)
    with s1:
        retention_lift = st.slider("Repeat Rate Improvement (%)",
                                   0, 30, 10, key="ret_lift")
    with s2:
        aov_lift = st.slider("AOV Increase (%)", 0, 50, 20, key="aov_lift")
    with s3:
        user_growth = st.slider("New User Growth (%)", 0, 100, 25, key="usr_growth")

    new_repeat_rev    = total_revenue * (retention_lift / 100) * 0.5
    new_aov_rev       = total_revenue * (aov_lift / 100)
    new_user_rev      = total_revenue * (user_growth / 100) * 0.4
    total_new_rev     = total_revenue + new_repeat_rev + new_aov_rev + new_user_rev

    scenarios = pd.DataFrame({
        "Scenario": ["Current", "Better Retention", "+ Higher AOV", "+ User Growth", "Combined"],
        "Revenue":  [total_revenue,
                     total_revenue + new_repeat_rev,
                     total_revenue + new_aov_rev,
                     total_revenue + new_user_rev,
                     total_new_rev],
    })
    fig = go.Figure(go.Bar(
        x=scenarios["Scenario"], y=scenarios["Revenue"],
        marker_color=["#4A5568","#4FD1C5","#63B3ED","#B794F4","#68D391"],
        text=[f"${r:,.0f}" for r in scenarios["Revenue"]],
        textposition="outside", textfont=dict(color="#EDF2F7", size=11),
        hovertemplate="<b>%{x}</b><br>$%{y:,.0f}<extra></extra>",
    ))
    T(fig, "Revenue Projection by Growth Lever")
    fig.update_layout(yaxis=dict(tickprefix="$", tickformat=","))
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

    uplift = total_new_rev - total_revenue
    st.markdown(f"""
<div style='background:linear-gradient(135deg,rgba(104,211,145,.08),rgba(79,209,197,.04));
            border:1px solid rgba(104,211,145,.2);border-radius:14px;
            padding:1.2rem 1.8rem;margin-top:.5rem;display:flex;
            align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;'>
  <div>
    <div style='font-size:.65rem;color:#4A5568;letter-spacing:.1em;
                text-transform:uppercase;margin-bottom:.3rem;'>Combined Scenario Uplift</div>
    <div style='font-family:Space Mono,monospace;font-size:1.8rem;
                font-weight:700;color:#68D391;'>+${uplift:,.0f}</div>
    <div style='font-size:.78rem;color:#A0AEC0;margin-top:.2rem;'>
      {(uplift/total_revenue*100):.1f}% revenue increase from current baseline</div>
  </div>
  <div style='text-align:right;'>
    <div style='font-size:.65rem;color:#4A5568;text-transform:uppercase;
                letter-spacing:.1em;margin-bottom:.3rem;'>Projected Annual Revenue</div>
    <div style='font-family:Space Mono,monospace;font-size:1.4rem;
                font-weight:700;color:#EDF2F7;'>${total_new_rev:,.0f}</div>
  </div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════
st.markdown("""
<div class='dash-footer'>
  Built by <span style='color:#63B3ED;font-weight:700;'>Aditya</span>
  &nbsp;&middot;&nbsp; AI Business Intelligence Platform
  &nbsp;&middot;&nbsp; <span style='color:#4A5568;'>Streamlit + Plotly + Python Analytics</span>
</div>
""", unsafe_allow_html=True)