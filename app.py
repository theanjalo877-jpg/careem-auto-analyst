import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------------------------------------------------------------
# CAREEM FOOD UAE GROWTH AUTO-ANALYST
# Portfolio / screening project by Anjalo Theophine Wilson
#
# Data note:
# - data.csv is illustrative project data supplied with this repository.
# - Research benchmarks are public and separately cited in the app.
# - No internal Careem data is claimed or represented.
# ---------------------------------------------------------------------

st.set_page_config(
    page_title="Careem Food UAE Growth Auto-Analyst | Anjalo Theophine Wilson",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------
# PREMIUM VISUAL SYSTEM
# ---------------------------------------------------------------------

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

        :root {
            --bg: #05070a;
            --panel: #0b1016;
            --line: rgba(255,255,255,0.09);
            --text: #f5f7fa;
            --muted: #9ca7b5;
            --green: #22c55e;
            --cyan: #38bdf8;
            --amber: #f5b942;
            --red: #fb7185;
        }

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif !important;
        }

        .stApp {
            background:
                radial-gradient(circle at 88% 8%, rgba(16,185,129,0.10), transparent 30%),
                radial-gradient(circle at 8% 35%, rgba(56,189,248,0.05), transparent 26%),
                var(--bg) !important;
            color: var(--text) !important;
        }

        .block-container {
            max-width: 1450px;
            padding-top: 1.2rem;
            padding-bottom: 4rem;
        }

        [data-testid="stSidebar"] {
            background: #070b10 !important;
            border-right: 1px solid var(--line);
        }

        [data-testid="stSidebar"] * {
            font-family: 'DM Sans', sans-serif !important;
        }

        h1, h2, h3, h4 {
            font-family: 'Space Grotesk', sans-serif !important;
            letter-spacing: -0.035em;
        }

        .hero {
            position: relative;
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: 26px;
            padding: 42px 44px 38px 44px;
            margin: 8px 0 24px 0;
            background:
                linear-gradient(135deg, rgba(255,255,255,0.045), rgba(255,255,255,0.012)),
                #080c11;
            box-shadow: 0 30px 90px rgba(0,0,0,0.30);
        }

        .hero::before,
        .hero::after {
            content: "";
            position: absolute;
            width: 420px;
            height: 420px;
            border-radius: 50%;
            filter: blur(70px);
            pointer-events: none;
            animation: drift 12s ease-in-out infinite alternate;
        }

        .hero::before {
            right: -190px;
            top: -230px;
            background: rgba(16,185,129,0.14);
        }

        .hero::after {
            left: -240px;
            bottom: -280px;
            background: rgba(56,189,248,0.07);
            animation-delay: -5s;
        }

        @keyframes drift {
            from { transform: translate3d(-12px, 8px, 0) scale(0.98); }
            to { transform: translate3d(18px, -14px, 0) scale(1.05); }
        }

        .eyebrow {
            position: relative;
            z-index: 1;
            color: var(--green);
            font-family: 'DM Mono', monospace !important;
            font-size: 0.74rem;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            margin-bottom: 12px;
        }

        .hero-title {
            position: relative;
            z-index: 1;
            font-family: 'Space Grotesk', sans-serif !important;
            font-size: clamp(2.5rem, 5vw, 5.3rem);
            line-height: 0.93;
            font-weight: 700;
            margin: 0;
            color: #ffffff;
        }

        .hero-title span {
            color: var(--green);
        }

        .hero-copy {
            position: relative;
            z-index: 1;
            max-width: 820px;
            color: #cbd5e1;
            font-size: 1.02rem;
            line-height: 1.7;
            margin-top: 20px;
        }

        .hero-meta {
            position: relative;
            z-index: 1;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 24px;
        }

        .tag {
            border: 1px solid var(--line);
            background: rgba(255,255,255,0.035);
            color: #dbe3ec;
            border-radius: 999px;
            padding: 7px 11px;
            font-family: 'DM Mono', monospace !important;
            font-size: 0.72rem;
        }

        .section-label {
            color: var(--muted);
            font-family: 'DM Mono', monospace !important;
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            margin-bottom: 7px;
        }

        .research-card,
        .insight-card,
        .metric-card,
        .source-card {
            border: 1px solid var(--line);
            border-radius: 18px;
            background: linear-gradient(145deg, rgba(255,255,255,0.04), rgba(255,255,255,0.012));
            padding: 20px;
            min-height: 100%;
        }

        .metric-value {
            font-family: 'Space Grotesk', sans-serif !important;
            font-size: 2rem;
            font-weight: 700;
            color: #ffffff;
        }

        .metric-label {
            color: var(--muted);
            font-size: 0.80rem;
            margin-top: 3px;
        }

        .metric-note {
            color: var(--green);
            font-family: 'DM Mono', monospace !important;
            font-size: 0.68rem;
            margin-top: 10px;
        }

        .insight-number {
            color: var(--green);
            font-family: 'DM Mono', monospace !important;
            font-size: 0.72rem;
        }

        .insight-title {
            font-family: 'Space Grotesk', sans-serif !important;
            font-size: 1.05rem;
            font-weight: 600;
            color: #ffffff;
            margin-top: 6px;
        }

        .insight-copy {
            color: #aeb8c5;
            font-size: 0.90rem;
            line-height: 1.6;
            margin-top: 8px;
        }

        .source-title {
            color: #ffffff;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 600;
            font-size: 0.98rem;
        }

        .source-copy {
            color: #aeb8c5;
            font-size: 0.82rem;
            line-height: 1.55;
            margin-top: 7px;
        }

        .source-ref {
            color: var(--green);
            font-family: 'DM Mono', monospace !important;
            font-size: 0.70rem;
            margin-top: 10px;
            overflow-wrap: anywhere;
        }

        .method-note {
            border-left: 2px solid var(--green);
            background: rgba(34,197,94,0.05);
            padding: 13px 16px;
            color: #b9c4d0;
            font-size: 0.82rem;
            line-height: 1.55;
            border-radius: 0 12px 12px 0;
            margin: 12px 0 20px 0;
        }

        .footer {
            margin-top: 42px;
            padding-top: 18px;
            border-top: 1px solid var(--line);
            color: #758092;
            font-size: 0.72rem;
            line-height: 1.6;
        }

        div[data-baseweb="tab-list"] {
            gap: 8px;
            border-bottom: 1px solid var(--line);
        }

        button[data-baseweb="tab"] {
            font-family: 'Space Grotesk', sans-serif !important;
            color: #9ca7b5 !important;
            background: transparent !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: #ffffff !important;
        }

        div[data-testid="stMetric"] {
            background: rgba(255,255,255,0.025);
            border: 1px solid var(--line);
            padding: 15px;
            border-radius: 15px;
        }

        .stButton > button {
            border: 1px solid rgba(34,197,94,0.28) !important;
            background: rgba(34,197,94,0.08) !important;
            color: #dfffea !important;
            border-radius: 10px !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 600 !important;
        }

        .stButton > button:hover {
            border-color: rgba(34,197,94,0.55) !important;
            background: rgba(34,197,94,0.14) !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------
# DATA LOADING
# ---------------------------------------------------------------------

@st.cache_data
def load_data():
    data = pd.read_csv("data.csv")

    required_columns = {
        "customer_id",
        "city",
        "orders",
        "revenue",
        "acquisition_channel",
        "last_order_days",
        "discount_used",
        "delivery_time",
        "cancellations",
    }

    missing = required_columns.difference(data.columns)

    if missing:
        raise ValueError(
            "data.csv is missing required columns: "
            + ", ".join(sorted(missing))
        )

    return data


try:
    df = load_data()
except Exception as exc:
    st.error(f"Data loading failed: {exc}")
    st.stop()

# ---------------------------------------------------------------------
# SIDEBAR CONTROLS
# ---------------------------------------------------------------------

st.sidebar.markdown("## CONTROL PANEL")
st.sidebar.caption(
    "Filters affect the project dataset. Scenario inputs are separated from observed data."
)

cities = sorted(df["city"].dropna().unique().tolist())
channels = sorted(df["acquisition_channel"].dropna().unique().tolist())

selected_cities = st.sidebar.multiselect(
    "Markets",
    options=cities,
    default=cities,
)

selected_channels = st.sidebar.multiselect(
    "Acquisition channels",
    options=channels,
    default=channels,
)

scenario_spend = st.sidebar.number_input(
    "Scenario: monthly marketing spend (AED)",
    min_value=0.0,
    value=10000.0,
    step=500.0,
)

scenario_new_customers = st.sidebar.number_input(
    "Scenario: new customers acquired",
    min_value=1,
    value=100,
    step=10,
)

scenario_margin = st.sidebar.slider(
    "Scenario: contribution margin",
    min_value=0.05,
    max_value=0.80,
    value=0.35,
    step=0.01,
)

scenario_monthly_orders = st.sidebar.number_input(
    "Scenario: orders per active customer / month",
    min_value=0.1,
    value=3.0,
    step=0.1,
)

scenario_lifetime_months = st.sidebar.number_input(
    "Scenario: customer lifetime (months)",
    min_value=1,
    value=12,
    step=1,
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Scenario metrics are modelling assumptions, not Careem internal figures."
)

filtered = df[
    df["city"].isin(selected_cities)
    & df["acquisition_channel"].isin(selected_channels)
].copy()

if filtered.empty:
    st.warning(
        "No records match the selected filters. Select at least one market "
        "and one channel."
    )
    st.stop()

# ---------------------------------------------------------------------
# OBSERVED DATA METRICS
# ---------------------------------------------------------------------

customers = filtered["customer_id"].nunique()
orders = int(filtered["orders"].sum())
revenue = float(filtered["revenue"].sum())
aov = revenue / orders if orders else 0.0
arpu = revenue / customers if customers else 0.0
opu = orders / customers if customers else 0.0
avg_delivery = float(filtered["delivery_time"].mean())
cancel_rate = float(filtered["cancellations"].mean())

at_risk = filtered[filtered["last_order_days"] >= 30]
at_risk_rate = len(at_risk) / customers if customers else 0.0

# Scenario unit economics.
cac = scenario_spend / scenario_new_customers

scenario_ltv = (
    aov
    * scenario_monthly_orders
    * scenario_margin
    * scenario_lifetime_months
)

ltv_cac = scenario_ltv / cac if cac > 0 else 0.0
cltv = scenario_ltv
scenario_arpu = aov * scenario_monthly_orders

# ---------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------

st.markdown(
    """
    <section class="hero">
        <div class="eyebrow">Growth intelligence / UAE food delivery</div>
        <h1 class="hero-title">
            Careem Food<br>
            <span>Growth Auto-Analyst</span>
        </h1>
        <p class="hero-copy">
            A portfolio-grade analytics system that turns customer, channel and
            operational telemetry into growth decisions. The model combines
            performance reporting, customer intelligence, unit economics,
            experimentation and market research rather than presenting charts alone.
        </p>
        <div class="hero-meta">
            <span class="tag">Business Analytics</span>
            <span class="tag">Digital Analytics</span>
            <span class="tag">Customer Experience</span>
            <span class="tag">Growth Strategy</span>
            <span class="tag">CAC / LTV / CLTV</span>
            <span class="tag">Cohort Analysis</span>
            <span class="tag">A/B Testing</span>
            <span class="tag">Decision Intelligence</span>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="method-note">
        <strong>Methodology:</strong> The repository dataset is a small illustrative
        dataset created for the portfolio challenge. Public research is used only
        for external market context. No confidential Careem data is claimed, and
        no public benchmark is substituted into the project dataset.
    </div>
    """,
    unsafe_allow_html=True,
)

tabs = st.tabs(
    [
        "Executive Overview",
        "Growth Economics",
        "Customer Intelligence",
        "Experimentation",
        "Market Intelligence",
        "References",
    ]
)

# ---------------------------------------------------------------------
# TAB 1: EXECUTIVE OVERVIEW
# ---------------------------------------------------------------------

with tabs[0]:
    st.markdown(
        '<div class="section-label">01 / Executive overview</div>',
        unsafe_allow_html=True,
    )
    st.title("Performance at a glance")

    metric_cols = st.columns(5)

    metrics = [
        ("Revenue", f"AED {revenue:,.0f}", "Observed project data"),
        ("Orders", f"{orders:,}", "Observed project data"),
        ("AOV", f"AED {aov:,.2f}", "Revenue / orders"),
        ("ARPU", f"AED {arpu:,.2f}", "Revenue / customer"),
        ("OPU", f"{opu:,.2f}", "Orders / customer"),
    ]

    for col, (label, value, note) in zip(metric_cols, metrics):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-note">{note}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("### Performance matrix")

    left_chart, right_chart = st.columns(2)

    with left_chart:
        city_channel = (
            filtered.groupby(
                ["city", "acquisition_channel"],
                as_index=False,
            )["revenue"]
            .sum()
        )

        fig = px.bar(
            city_channel,
            x="city",
            y="revenue",
            color="acquisition_channel",
            barmode="stack",
            template="plotly_dark",
            title="Revenue by market and acquisition channel",
            labels={
                "city": "Market",
                "revenue": "Revenue (AED)",
                "acquisition_channel": "Channel",
            },
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend_title_text="",
            margin=dict(l=10, r=10, t=55, b=10),
        )

        st.plotly_chart(fig, use_container_width=True)

    with right_chart:
        channel_orders = (
            filtered.groupby(
                "acquisition_channel",
                as_index=False,
            )["orders"]
            .sum()
            .sort_values("orders", ascending=False)
        )

        fig = px.bar(
            channel_orders,
            x="orders",
            y="acquisition_channel",
            orientation="h",
            template="plotly_dark",
            title="Order volume by acquisition channel",
            labels={
                "orders": "Orders",
                "acquisition_channel": "Channel",
            },
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=10, r=10, t=55, b=10),
            yaxis=dict(categoryorder="total ascending"),
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Decision layer")

    decision_cols = st.columns(3)

    decisions = [
        (
            "01",
            "Protect frequency before chasing volume",
            f"The observed dataset averages {opu:.2f} orders per customer. "
            "Growth should be evaluated on repeat behaviour, not acquisition "
            "volume alone.",
        ),
        (
            "02",
            "Treat delivery reliability as a growth variable",
            f"Average observed delivery time is {avg_delivery:.1f} minutes "
            f"and the observed cancellation rate is {cancel_rate:.1%}. "
            "Both should sit beside commercial metrics.",
        ),
        (
            "03",
            "Separate acquisition efficiency from customer value",
            "ARPU and OPU can be calculated directly from the project data, "
            "while CAC and LTV require explicit assumptions rather than "
            "fabricated source data.",
        ),
    ]

    for col, (number, title, copy) in zip(decision_cols, decisions):
        with col:
            st.markdown(
                f"""
                <div class="insight-card">
                    <div class="insight-number">{number}</div>
                    <div class="insight-title">{title}</div>
                    <div class="insight-copy">{copy}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------------------
# TAB 2: GROWTH ECONOMICS
# ---------------------------------------------------------------------

with tabs[1]:
    st.markdown(
        '<div class="section-label">02 / Growth economics</div>',
        unsafe_allow_html=True,
    )
    st.title("CAC, LTV, ARPU, OPU and CLTV")

    st.markdown(
        """
        <div class="method-note">
            CAC, LTV and CLTV are scenario-modelled because the repository does not
            contain paid-media spend, gross margin, retention duration or acquisition
            counts. ARPU and OPU are calculated directly from the supplied project data.
        </div>
        """,
        unsafe_allow_html=True,
    )

    econ_cols = st.columns(5)

    econ_metrics = [
        ("CAC", f"AED {cac:,.2f}", "Scenario spend / new customers"),
        (
            "LTV",
            f"AED {scenario_ltv:,.2f}",
            "AOV × frequency × margin × lifetime",
        ),
        ("LTV / CAC", f"{ltv_cac:.2f}x", "Scenario efficiency"),
        (
            "Scenario ARPU",
            f"AED {scenario_arpu:,.2f}",
            "AOV × monthly frequency",
        ),
        ("CLTV", f"AED {cltv:,.2f}", "Modelled customer value"),
    ]

    for col, (label, value, note) in zip(econ_cols, econ_metrics):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-note">{note}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("### Unit economics sensitivity")

    frequencies = np.linspace(
        max(0.5, scenario_monthly_orders - 1.5),
        scenario_monthly_orders + 1.5,
        7,
    )

    sensitivity = pd.DataFrame(
        {
            "Monthly orders / customer": frequencies,
            "Scenario LTV": [
                aov
                * frequency
                * scenario_margin
                * scenario_lifetime_months
                for frequency in frequencies
            ],
        }
    )

    fig = px.line(
        sensitivity,
        x="Monthly orders / customer",
        y="Scenario LTV",
        markers=True,
        template="plotly_dark",
        title="How customer frequency changes modelled lifetime value",
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=55, b=10),
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Metric definitions")

    definitions = pd.DataFrame(
        {
            "Metric": ["CAC", "LTV", "ARPU", "OPU", "CLTV"],
            "Definition": [
                "Customer acquisition cost: acquisition spend divided by acquired customers.",
                "Lifetime value: modelled value created by a customer over an assumed lifetime.",
                "Average revenue per user/customer.",
                "Orders per user/customer.",
                "Customer lifetime value using the explicit scenario model.",
            ],
            "Data status": [
                "Scenario",
                "Scenario",
                "Observed",
                "Observed",
                "Scenario",
            ],
        }
    )

    st.dataframe(
        definitions,
        use_container_width=True,
        hide_index=True,
    )

# ---------------------------------------------------------------------
# TAB 3: CUSTOMER INTELLIGENCE
# ---------------------------------------------------------------------

with tabs[2]:
    st.markdown(
        '<div class="section-label">03 / Customer intelligence</div>',
        unsafe_allow_html=True,
    )
    st.title("Cohort analysis, churn / attrition modelling and lifecycle")

    st.markdown(
        """
        <div class="method-note">
            The repository contains recency, order frequency, revenue and cancellation
            fields. It does not contain true acquisition dates, so the lifecycle view
            uses transparent recency cohorts rather than pretending they are acquisition
            cohorts. The 31+ day group is an at-risk heuristic, not a contractual churn definition.
        </div>
        """,
        unsafe_allow_html=True,
    )

    def recency_bucket(days):
        if days <= 7:
            return "0–7 days"
        if days <= 14:
            return "8–14 days"
        if days <= 30:
            return "15–30 days"
        return "31+ days"

    lifecycle = filtered.copy()
    lifecycle["recency_cohort"] = lifecycle["last_order_days"].apply(
        recency_bucket
    )

    cohort_summary = (
        lifecycle.groupby(
            "recency_cohort",
            as_index=False,
        )
        .agg(
            customers=("customer_id", "nunique"),
            orders=("orders", "sum"),
            revenue=("revenue", "sum"),
            avg_delivery=("delivery_time", "mean"),
            cancellations=("cancellations", "sum"),
        )
    )

    cohort_order = [
        "0–7 days",
        "8–14 days",
        "15–30 days",
        "31+ days",
    ]

    cohort_summary["recency_cohort"] = pd.Categorical(
        cohort_summary["recency_cohort"],
        categories=cohort_order,
        ordered=True,
    )

    cohort_summary = cohort_summary.sort_values("recency_cohort")

    left_chart, right_chart = st.columns(2)

    with left_chart:
        fig = px.bar(
            cohort_summary,
            x="recency_cohort",
            y="customers",
            template="plotly_dark",
            title="Customer recency distribution",
            labels={
                "recency_cohort": "Last-order recency",
                "customers": "Customers",
            },
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=10, r=10, t=55, b=10),
        )

        st.plotly_chart(fig, use_container_width=True)

    with right_chart:
        fig = px.bar(
            cohort_summary,
            x="recency_cohort",
            y="revenue",
            template="plotly_dark",
            title="Revenue exposure by recency cohort",
            labels={
                "recency_cohort": "Last-order recency",
                "revenue": "Revenue (AED)",
            },
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=10, r=10, t=55, b=10),
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Churn / attrition signal")

    churn_cols = st.columns(3)

    churn_metrics = [
        (
            "At-risk customers",
            f"{len(at_risk):,}",
            "Recency heuristic: 31+ days",
        ),
        (
            "At-risk rate",
            f"{at_risk_rate:.1%}",
            "Not a contractual churn definition",
        ),
        (
            "Cancellations",
            f"{int(filtered['cancellations'].sum()):,}",
            "Observed records",
        ),
    ]

    for col, (label, value, note) in zip(churn_cols, churn_metrics):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-note">{note}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("### Customer value map")

    customer_view = (
        filtered.groupby(
            "customer_id",
            as_index=False,
        )
        .agg(
            orders=("orders", "sum"),
            revenue=("revenue", "sum"),
            last_order_days=("last_order_days", "min"),
            delivery_time=("delivery_time", "mean"),
            cancellations=("cancellations", "sum"),
        )
    )

    customer_view["segment"] = np.select(
        [
            (
                (customer_view["orders"] >= 10)
                & (customer_view["last_order_days"] <= 14)
            ),
            customer_view["last_order_days"] >= 31,
            customer_view["orders"] <= 2,
        ],
        [
            "High-value active",
            "At-risk / dormant",
            "Low-frequency",
        ],
        default="Core active",
    )

    fig = px.scatter(
        customer_view,
        x="orders",
        y="revenue",
        size="revenue",
        color="segment",
        hover_data=[
            "customer_id",
            "last_order_days",
            "delivery_time",
        ],
        template="plotly_dark",
        title="Customer frequency vs. revenue",
        labels={
            "orders": "Orders",
            "revenue": "Revenue (AED)",
            "segment": "Lifecycle segment",
        },
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=55, b=10),
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------------
# TAB 4: EXPERIMENTATION
# ---------------------------------------------------------------------

with tabs[3]:
    st.markdown(
        '<div class="section-label">04 / Experimentation</div>',
        unsafe_allow_html=True,
    )
    st.title("A/B testing and conversion-rate logic")

    st.markdown(
        """
        <div class="method-note">
            A/B testing requires exposure counts, conversions and an experiment design.
            The controls below are a simulation layer for demonstrating the analytical
            method; they are not historical Careem experiment results.
        </div>
        """,
        unsafe_allow_html=True,
    )

    control_exposed = st.number_input(
        "Control exposed",
        min_value=100,
        value=5000,
        step=500,
    )

    control_converted = st.number_input(
        "Control conversions",
        min_value=0,
        value=350,
        step=10,
    )

    test_exposed = st.number_input(
        "Test exposed",
        min_value=100,
        value=5000,
        step=500,
    )

    test_converted = st.number_input(
        "Test conversions",
        min_value=0,
        value=420,
        step=10,
    )

    control_rate = control_converted / control_exposed
    test_rate = test_converted / test_exposed
    uplift = (
        (test_rate / control_rate - 1)
        if control_rate
        else 0.0
    )

    ab_cols = st.columns(4)

    ab_metrics = [
        ("Control CVR", f"{control_rate:.2%}"),
        ("Test CVR", f"{test_rate:.2%}"),
        ("Relative uplift", f"{uplift:.1%}"),
        (
            "Incremental conversions",
            f"{max(0, test_converted - control_converted):,}",
        ),
    ]

    for col, (label, value) in zip(ab_cols, ab_metrics):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-note">Simulation</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    experiment_df = pd.DataFrame(
        {
            "Variant": ["Control", "Test"],
            "Exposed": [control_exposed, test_exposed],
            "Conversions": [
                control_converted,
                test_converted,
            ],
            "Conversion rate": [
                control_rate,
                test_rate,
            ],
        }
    )

    fig = px.bar(
        experiment_df,
        x="Variant",
        y="Conversion rate",
        text="Conversion rate",
        template="plotly_dark",
        title="A/B conversion comparison",
    )

    fig.update_traces(
        texttemplate="%{text:.2%}",
        textposition="outside",
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_tickformat=".0%",
        margin=dict(l=10, r=10, t=55, b=10),
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Experiment design checklist")

    st.dataframe(
        pd.DataFrame(
            {
                "Stage": [
                    "Hypothesis",
                    "Primary metric",
                    "Guardrail metrics",
                    "Randomisation",
                    "Sample size",
                    "Decision rule",
                ],
                "Implementation": [
                    "State one causal change and the expected behavioural mechanism.",
                    "Use conversion rate or another pre-defined outcome.",
                    "Monitor cancellation, delivery time, margin and customer complaints.",
                    "Split eligible users without systematic selection bias.",
                    "Predefine minimum exposure before reading the result.",
                    "Do not ship on uplift alone; check significance, guardrails and economics.",
                ],
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

# ---------------------------------------------------------------------
# TAB 5: MARKET INTELLIGENCE
# ---------------------------------------------------------------------

with tabs[4]:
    st.markdown(
        '<div class="section-label">05 / Market intelligence</div>',
        unsafe_allow_html=True,
    )
    st.title("UAE food delivery: external research context")

    st.markdown(
        """
        <div class="method-note">
            This section separates public market intelligence from the portfolio
            dataset. It demonstrates how an analyst combines internal telemetry
            with external evidence before making a growth recommendation.
        </div>
        """,
        unsafe_allow_html=True,
    )

    research_cards = [
        (
            "R1",
            "Careem platform scale",
            "Careem states that it serves more than 50 million customers, operates in 70+ cities across 10 countries, and is building an Everything App spanning mobility, food, groceries, payments and other services.",
            "Careem About Us",
        ),
        (
            "R2",
            "Food assortment and demand",
            "Careem's UAE Food page currently advertises access to 9,500 restaurants. Careem also reported a 36% increase in Food order volume during Suhoor hours in March 2025 versus February.",
            "Careem Food; Careem Ramadan 2025",
        ),
        (
            "R3",
            "Subscription and retention",
            "Careem Plus is positioned as a cross-service subscription. Careem says members save AED 300+ per month on average, with Food benefits including free delivery on qualifying orders and member discounts.",
            "Careem Plus",
        ),
        (
            "R4",
            "UAE digital readiness",
            "DataReportal reported 11.1 million internet users in the UAE in January 2025, equivalent to 99% internet penetration, alongside 11.3 million social-media user identities.",
            "DataReportal Digital 2025: UAE",
        ),
        (
            "R5",
            "Convenience and ready-to-eat demand",
            "McKinsey's 2026 MENA grocery research found food-to-go growth continued to outpace total grocery growth, with younger consumers showing stronger intent toward ready-to-eat options.",
            "McKinsey, State of Grocery Retail MENA 2026",
        ),
        (
            "R6",
            "Last-mile optimisation",
            "A 2025 research study using more than 8 million Dubai grocery orders found that adding five minutes of delivery-time flexibility reduced daily delivery mileage by about 30% and lifecycle CO2 emissions by about 20%.",
            "Eshtiyagh et al., 2025",
        ),
    ]

    research_cols = st.columns(2)

    for index, (ref, title, copy, source) in enumerate(research_cards):
        with research_cols[index % 2]:
            st.markdown(
                f"""
                <div class="research-card">
                    <div class="insight-number">{ref}</div>
                    <div class="insight-title">{title}</div>
                    <div class="insight-copy">{copy}</div>
                    <div class="source-ref">{source}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("### Competitive landscape")

    competitive = pd.DataFrame(
        {
            "Platform": [
                "Careem Food",
                "Talabat",
                "noon Food",
            ],
            "Public positioning signal": [
                "Everything App + Food + subscription ecosystem",
                "Broad UAE food, grocery and convenience marketplace",
                "Food delivery + broader noon ecosystem and restaurant network",
            ],
            "Analytical implication": [
                "Cross-service retention and subscription economics can reduce dependence on single-order economics.",
                "Breadth and geographic coverage make assortment, delivery reliability and merchant density important battlegrounds.",
                "Ecosystem scale and restaurant acquisition increase pressure on price, convenience and availability.",
            ],
            "Evidence": [
                "Careem public pages",
                "Talabat UAE public pages",
                "noon Food partner page",
            ],
        }
    )

    st.dataframe(
        competitive,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("### What the evidence suggests")

    implication_cols = st.columns(3)

    implications = [
        (
            "01",
            "Retention is a strategic lever",
            "Subscription, cross-service usage and repeat ordering create reasons to optimise LTV and frequency, not just acquisition.",
        ),
        (
            "02",
            "Convenience must be measured as a system",
            "Delivery time, cancellation, assortment, price and customer effort interact. A single KPI can hide a weak customer experience.",
        ),
        (
            "03",
            "Growth should be locally segmented",
            "UAE behaviour is highly digital, but market, time-of-day, cuisine, customer lifecycle and value sensitivity can differ materially.",
        ),
    ]

    for col, (number, title, copy) in zip(
        implication_cols,
        implications,
    ):
        with col:
            st.markdown(
                f"""
                <div class="insight-card">
                    <div class="insight-number">{number}</div>
                    <div class="insight-title">{title}</div>
                    <div class="insight-copy">{copy}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------------------
# TAB 6: REFERENCES
# ---------------------------------------------------------------------

with tabs[5]:
    st.markdown(
        '<div class="section-label">06 / References</div>',
        unsafe_allow_html=True,
    )
    st.title("Research and source register")

    st.markdown(
        """
        <div class="method-note">
            Citation style: numbered source register with organisation or author,
            publication title, publication date where available, and direct URL.
            Public-source claims are not presented as Careem internal data.
        </div>
        """,
        unsafe_allow_html=True,
    )

    references = [
        (
            "[1]",
            "Careem",
            "About Us",
            "Careem's public company profile and platform scale.",
            "https://www.careem.com/en-AE/about-us/",
        ),
        (
            "[2]",
            "Careem",
            "Food - Always eat on time",
            "Current public UAE Food proposition and restaurant assortment.",
            "https://www.careem.com/en-AE/food/",
        ),
        (
            "[3]",
            "Careem",
            "Ramadan 2025 with Careem",
            "Public Food order-volume and UAE behavioural observations.",
            "https://blog.careem.com/posts/ramadan-trends-2025",
        ),
        (
            "[4]",
            "Careem",
            "Careem Plus",
            "Public subscription benefits and member-value proposition.",
            "https://www.careem.com/en-AE/cplus/",
        ),
        (
            "[5]",
            "Careem",
            "Pricing and fees",
            "Public UAE Food service-fee and delivery-fee information.",
            "https://help.careem.com/hc/en-us/articles/8675020815251-Pricing-and-fees",
        ),
        (
            "[6]",
            "Careem",
            "Introducing Scheduling on Careem Food",
            "Public product rationale around meal-time demand and planning.",
            "https://blog.careem.com/posts/introducing-scheduling-on-careem-food",
        ),
        (
            "[7]",
            "DataReportal / Kepios",
            "Digital 2025: The United Arab Emirates",
            "UAE internet, mobile and social-media adoption context.",
            "https://datareportal.com/reports/digital-2025-united-arab-emirates",
        ),
        (
            "[8]",
            "U.S. Department of Commerce",
            "United Arab Emirates - eCommerce",
            "UAE e-commerce environment and consumer considerations.",
            "https://www.trade.gov/country-commercial-guides/united-arab-emirates-ecommerce",
        ),
        (
            "[9]",
            "McKinsey & Company",
            "State of grocery retail MENA 2026: Managing the growth paradox",
            "MENA food-to-go and ready-to-eat consumer trends.",
            "https://www.mckinsey.com/industries/retail/our-insights/state-of-grocery-retail-mena-2026-managing-the-growth-paradox",
        ),
        (
            "[10]",
            "J. Eshtiyagh et al.",
            "The Value of Patience in Online Grocery Shopping",
            "2025 research using 8+ million Dubai grocery orders and last-mile optimisation findings.",
            "https://arxiv.org/abs/2510.19066",
        ),
        (
            "[11]",
            "Talabat UAE",
            "Food delivery from your nearest restaurants in UAE",
            "Public competitor footprint and proposition.",
            "https://ae.talabat.com/",
        ),
        (
            "[12]",
            "noon Food",
            "Grow your restaurant business with noon Food",
            "Public competitor restaurant-network positioning.",
            "https://food-partners.noon.com/uae-en/",
        ),
        (
            "[13]",
            "GitHub",
            "careem-auto-analyst",
            "Project repository and reproducible code.",
            "https://github.com/theanjalo877-jpg/careem-auto-analyst",
        ),
    ]

    for ref, organisation, title, description, url in references:
        st.markdown(
            f"""
            <div class="source-card" style="margin-bottom:10px;">
                <div class="source-title">
                    {ref} {organisation} — {title}
                </div>
                <div class="source-copy">
                    {description}
                </div>
                <div class="source-ref">
                    {url}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Data provenance")

    st.dataframe(
        pd.DataFrame(
            {
                "Layer": [
                    "Project telemetry",
                    "Calculated metrics",
                    "Scenario modelling",
                    "External research",
                ],
                "Source": [
                    "data.csv in this repository",
                    "Derived from data.csv",
                    "User-adjustable assumptions in sidebar",
                    "Public sources listed above",
                ],
                "Confidential Careem data used": [
                    "No",
                    "No",
                    "No",
                    "No",
                ],
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

# ---------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        <strong>Careem Food UAE Growth Auto-Analyst</strong><br>
        Portfolio project by Anjalo Theophine Wilson. Built to demonstrate
        business analytics, digital analytics, customer intelligence, growth
        economics, experimentation, research synthesis and decision storytelling.
        Public research is cited separately from the illustrative project dataset.
    </div>
    """,
    unsafe_allow_html=True,
)
