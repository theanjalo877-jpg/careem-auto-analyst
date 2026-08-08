import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# 1. GLOBAL CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Careem Food Growth Intelligence | Anjalo Theophine Wilson",
    page_icon="●",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# 2. PREMIUM DESIGN SYSTEM
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* ---------------------------------------------------------
   ROOT
--------------------------------------------------------- */

:root {
    --bg: #05070a;
    --panel: #0b1016;
    --panel-2: #10161e;
    --panel-3: #151c25;
    --line: rgba(255,255,255,0.09);

    --green: #00d084;
    --green-soft: #7ce8b8;
    --white: #f5f7fa;
    --muted: #8f9baa;
    --muted-2: #647080;

    --blue: #4da3ff;
    --amber: #f5b942;
    --red: #ff6673;
}

/* ---------------------------------------------------------
   GLOBAL
--------------------------------------------------------- */

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 85% 5%,
            rgba(0,208,132,0.10),
            transparent 25%
        ),
        radial-gradient(
            circle at 10% 80%,
            rgba(77,163,255,0.06),
            transparent 25%
        ),
        #05070a;
    color: var(--white);
}

/* Subtle animated atmosphere */

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;

    background-image:
        linear-gradient(
            rgba(255,255,255,0.018) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(255,255,255,0.018) 1px,
            transparent 1px
        );

    background-size: 70px 70px;

    mask-image:
        linear-gradient(
            to bottom,
            black,
            transparent 85%
        );

    animation: gridMove 18s linear infinite;
}

@keyframes gridMove {
    from {
        transform: translate3d(0,0,0);
    }
    to {
        transform: translate3d(70px,70px,0);
    }
}

.block-container {
    position: relative;
    z-index: 1;
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* ---------------------------------------------------------
   SIDEBAR
--------------------------------------------------------- */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #080b10 0%,
            #05070a 100%
        );
    border-right: 1px solid var(--line);
}

section[data-testid="stSidebar"] * {
    font-family: "DM Sans", sans-serif;
}

.sidebar-brand {
    padding: 0.5rem 0 1.5rem 0;
}

.sidebar-brand .small {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.65rem;
    letter-spacing: 0.16em;
    color: var(--green);
    text-transform: uppercase;
}

.sidebar-brand .title {
    font-family: "Space Grotesk", sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--white);
    margin-top: 0.35rem;
}

/* ---------------------------------------------------------
   HERO
--------------------------------------------------------- */

.hero {
    padding: 3rem 0 2.5rem 0;
    border-bottom: 1px solid var(--line);
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: "";
    position: absolute;
    width: 320px;
    height: 320px;
    right: -100px;
    top: -160px;

    background:
        radial-gradient(
            circle,
            rgba(0,208,132,0.18),
            transparent 68%
        );

    animation: pulseGlow 6s ease-in-out infinite;
}

@keyframes pulseGlow {
    0%, 100% {
        opacity: 0.55;
        transform: scale(0.95);
    }

    50% {
        opacity: 1;
        transform: scale(1.08);
    }
}

.eyebrow {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--green);
    margin-bottom: 1rem;
}

.hero h1 {
    font-family: "Space Grotesk", sans-serif !important;
    font-size: clamp(3rem, 6vw, 6rem) !important;
    line-height: 0.94 !important;
    letter-spacing: -0.055em !important;
    font-weight: 700 !important;

    background:
        linear-gradient(
            135deg,
            #ffffff 20%,
            #ccefe1 58%,
            #00d084 100%
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin: 0 !important;
}

.hero-subtitle {
    max-width: 780px;
    margin-top: 1.3rem;
    color: #b7c0ca;
    font-size: 1.05rem;
    line-height: 1.65;
}

.hero-meta {
    margin-top: 1.3rem;
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;

    font-family: "JetBrains Mono", monospace;
    font-size: 0.68rem;
    letter-spacing: 0.08em;
    color: var(--muted);
    text-transform: uppercase;
}

/* ---------------------------------------------------------
   SECTION HEADINGS
--------------------------------------------------------- */

.section-label {
    font-family: "JetBrains Mono", monospace;
    color: var(--green);
    font-size: 0.68rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.45rem;
}

.section-title {
    font-family: "Space Grotesk", sans-serif;
    font-size: 2rem;
    font-weight: 650;
    letter-spacing: -0.035em;
    color: var(--white);
    margin-bottom: 0.35rem;
}

.section-description {
    color: var(--muted);
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
}

/* ---------------------------------------------------------
   CARDS
--------------------------------------------------------- */

.premium-card {
    background:
        linear-gradient(
            145deg,
            rgba(20,27,36,0.96),
            rgba(8,12,17,0.96)
        );

    border: 1px solid var(--line);
    border-radius: 18px;

    padding: 1.45rem;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.20);

    transition:
        transform 0.25s ease,
        border-color 0.25s ease,
        box-shadow 0.25s ease;
}

.premium-card:hover {
    transform: translateY(-3px);
    border-color: rgba(0,208,132,0.30);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.35);
}

.card-kicker {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.62rem;
    letter-spacing: 0.12em;
    color: var(--muted-2);
    text-transform: uppercase;
}

.card-title {
    font-family: "Space Grotesk", sans-serif;
    font-size: 1.05rem;
    font-weight: 600;
    margin-top: 0.45rem;
    color: var(--white);
}

.card-text {
    color: #9da7b2;
    font-size: 0.86rem;
    line-height: 1.6;
    margin-top: 0.55rem;
}

/* ---------------------------------------------------------
   KPI CARDS
--------------------------------------------------------- */

.kpi-card {
    background:
        linear-gradient(
            145deg,
            #101720,
            #080c11
        );

    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 1.3rem;

    position: relative;
    overflow: hidden;
}

.kpi-card::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--green);
}

.kpi-label {
    color: var(--muted);
    font-family: "JetBrains Mono", monospace;
    font-size: 0.62rem;
    letter-spacing: 0.10em;
    text-transform: uppercase;
}

.kpi-value {
    font-family: "Space Grotesk", sans-serif;
    font-size: 2rem;
    font-weight: 650;
    letter-spacing: -0.04em;
    margin-top: 0.35rem;
    color: var(--white);
}

.kpi-note {
    color: var(--green-soft);
    font-size: 0.72rem;
    margin-top: 0.3rem;
}

/* ---------------------------------------------------------
   INSIGHT BOXES
--------------------------------------------------------- */

.insight {
    border-left: 2px solid var(--green);
    background: rgba(0,208,132,0.045);
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.15rem;
    margin: 0.75rem 0;
}

.insight-title {
    font-family: "Space Grotesk", sans-serif;
    font-weight: 600;
    color: var(--white);
}

.insight-text {
    color: #aab4bf;
    font-size: 0.84rem;
    line-height: 1.55;
    margin-top: 0.3rem;
}

/* ---------------------------------------------------------
   TABLE
--------------------------------------------------------- */

.dataframe {
    border-radius: 12px !important;
}

/* ---------------------------------------------------------
   SOURCE PANEL
--------------------------------------------------------- */

.source-item {
    border-bottom: 1px solid var(--line);
    padding: 1rem 0;
}

.source-number {
    font-family: "JetBrains Mono", monospace;
    color: var(--green);
    font-size: 0.65rem;
}

.source-title {
    font-family: "Space Grotesk", sans-serif;
    color: var(--white);
    font-weight: 600;
    margin-top: 0.2rem;
}

.source-description {
    color: var(--muted);
    font-size: 0.82rem;
    line-height: 1.5;
    margin-top: 0.25rem;
}

/* ---------------------------------------------------------
   BUTTONS
--------------------------------------------------------- */

.stButton > button {
    border-radius: 10px;
    border: 1px solid rgba(0,208,132,0.35);
    background: rgba(0,208,132,0.06);
    color: var(--white);
    font-family: "DM Sans", sans-serif;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: var(--green);
    background: rgba(0,208,132,0.12);
    color: var(--white);
}

/* ---------------------------------------------------------
   STREAMLIT ELEMENT CLEANUP
--------------------------------------------------------- */

div[data-testid="stMetric"] {
    background: transparent;
}

div[data-testid="stMetricLabel"] {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.62rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--muted);
}

div[data-testid="stMetricValue"] {
    font-family: "Space Grotesk", sans-serif;
}

hr {
    border-color: var(--line);
}

/* Hide unnecessary Streamlit decoration */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# 3. PLOTLY THEME
# ============================================================

PLOT_BG = "#0b1016"
PAPER_BG = "#05070a"
TEXT_COLOR = "#dce3ea"
GRID_COLOR = "rgba(255,255,255,0.07)"

CHANNEL_COLORS = {
    "Instagram Paid": "#E1306C",
    "Google Search": "#4DA3FF",
    "Organic Referral": "#00D084",
    "TikTok Brand": "#A855F7",
}


def apply_plotly_theme(fig):
    fig.update_layout(
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(
            family="DM Sans",
            color=TEXT_COLOR,
        ),
        title_font=dict(
            family="Space Grotesk",
            size=17,
            color="#F5F7FA",
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=11),
        ),
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=20,
        ),
        xaxis=dict(
            gridcolor=GRID_COLOR,
            zerolinecolor=GRID_COLOR,
        ),
        yaxis=dict(
            gridcolor=GRID_COLOR,
            zerolinecolor=GRID_COLOR,
        ),
    )

    return fig


# ============================================================
# 4. DATA LOADING
# ============================================================

def create_demo_dataset():
    """
    Creates a synthetic demonstration dataset.

    IMPORTANT:
    This is not Careem internal data.
    It exists only to demonstrate analytical methodology.
    """

    rng = np.random.default_rng(42)

    cities = [
        "Dubai",
        "Abu Dhabi",
        "Sharjah",
        "Ajman",
    ]

    channels = [
        "Instagram Paid",
        "Google Search",
        "Organic Referral",
        "TikTok Brand",
    ]

    months = pd.date_range(
        start="2026-01-01",
        periods=6,
        freq="MS",
    )

    rows = []

    for month in months:
        for city in cities:
            for channel in channels:

                sessions = int(
                    rng.integers(
                        900,
                        6500,
                    )
                )

                conversion_rate = float(
                    rng.uniform(
                        0.045,
                        0.115,
                    )
                )

                orders = max(
                    1,
                    int(
                        sessions
                        * conversion_rate
                    ),
                )

                aov = float(
                    rng.uniform(
                        52,
                        88,
                    )
                )

                revenue = orders * aov

                returning_rate = float(
                    rng.uniform(
                        0.22,
                        0.58,
                    )
                )

                new_users = max(
                    1,
                    int(
                        orders
                        * (1 - returning_rate)
                    ),
                )

                returning_users = max(
                    1,
                    orders - new_users,
                )

                rows.append(
                    {
                        "month": month,
                        "city": city,
                        "acquisition_channel": channel,
                        "sessions": sessions,
                        "orders": orders,
                        "revenue": round(
                            revenue,
                            2,
                        ),
                        "aov": round(
                            aov,
                            2,
                        ),
                        "new_users": new_users,
                        "returning_users": returning_users,
                    }
                )

    return pd.DataFrame(rows)


try:
    df = pd.read_csv("data.csv")

    DATA_MODE = "User-provided dataset"

except FileNotFoundError:
    df = create_demo_dataset()

    DATA_MODE = "Synthetic demonstration dataset"


# ============================================================
# 5. DATA NORMALISATION
# ============================================================

df.columns = [
    str(column).strip()
    for column in df.columns
]

required_columns = [
    "city",
    "acquisition_channel",
    "orders",
    "revenue",
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error(
        "The dataset is missing required columns: "
        + ", ".join(missing_columns)
    )
    st.stop()


if "sessions" not in df.columns:
    df["sessions"] = np.maximum(
        df["orders"] * 12,
        1,
    )

if "aov" not in df.columns:
    df["aov"] = np.where(
        df["orders"] > 0,
        df["revenue"] / df["orders"],
        0,
    )

if "new_users" not in df.columns:
    df["new_users"] = (
        df["orders"] * 0.65
    ).astype(int)

if "returning_users" not in df.columns:
    df["returning_users"] = (
        df["orders"] * 0.35
    ).astype(int)


# ============================================================
# 6. SIDEBAR NAVIGATION
# ============================================================

st.sidebar.markdown(
    """
<div class="sidebar-brand">
    <div class="small">Business Intelligence Portfolio</div>
    <div class="title">Growth Intelligence</div>
</div>
""",
    unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Executive Overview",
        "Growth Diagnostics",
        "Customer Funnel",
        "Experimentation",
        "Data Explorer",
        "Methodology & Sources",
    ],
)

st.sidebar.divider()

st.sidebar.markdown(
    """
<div class="card-kicker">
DATASET STATUS
</div>
""",
    unsafe_allow_html=True,
)

if DATA_MODE == "Synthetic demonstration dataset":
    st.sidebar.warning(
        "Synthetic demonstration data is active. "
        "No Careem internal data is used."
    )
else:
    st.sidebar.success(
        "User-provided dataset loaded."
    )


# ============================================================
# 7. FILTERS
# ============================================================

cities = sorted(
    df["city"].dropna().unique().tolist()
)

channels = sorted(
    df[
        "acquisition_channel"
    ]
    .dropna()
    .unique()
    .tolist()
)

with st.sidebar.expander(
    "ANALYSIS FILTERS",
    expanded=True,
):

    selected_cities = st.multiselect(
        "Cities",
        cities,
        default=cities,
    )

    selected_channels = st.multiselect(
        "Acquisition channels",
        channels,
        default=channels,
    )


filtered_df = df[
    df["city"].isin(
        selected_cities
    )
    & df["acquisition_channel"].isin(
        selected_channels
    )
].copy()


# ============================================================
# 8. COMMON METRICS
# ============================================================

total_revenue = float(
    filtered_df["revenue"].sum()
)

total_orders = int(
    filtered_df["orders"].sum()
)

total_sessions = int(
    filtered_df["sessions"].sum()
)

aov = (
    total_revenue / total_orders
    if total_orders > 0
    else 0
)

conversion_rate = (
    total_orders / total_sessions * 100
    if total_sessions > 0
    else 0
)

returning_users = int(
    filtered_df[
        "returning_users"
    ].sum()
)

new_users = int(
    filtered_df[
        "new_users"
    ].sum()
)

retention_mix = (
    returning_users
    /
    max(
        returning_users + new_users,
        1,
    )
    * 100
)


# ============================================================
# 9. HERO
# ============================================================

st.markdown(
    """
<div class="hero">

<div class="eyebrow">
CAREEM FOOD / GROWTH INTELLIGENCE CASE STUDY
</div>

<h1>
Growth<br>
Auto-Analyst
</h1>

<div class="hero-subtitle">
An analytical decision-support prototype designed to turn
growth telemetry into performance signals, customer insights,
experimentation priorities and practical business actions.
</div>

<div class="hero-meta">
<span>ANJALO THEOPHINE WILSON</span>
<span>BUSINESS ANALYTICS</span>
<span>DATA STORYTELLING</span>
<span>GROWTH STRATEGY</span>
</div>

</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# 10. EXECUTIVE OVERVIEW
# ============================================================

if page == "Executive Overview":

    st.markdown(
        """
<div class="section-label">
01 / Executive Overview
</div>

<div class="section-title">
From raw signals to business decisions
</div>

<div class="section-description">
A compact executive view of the selected market and acquisition mix.
</div>
""",
        unsafe_allow_html=True,
    )

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(
            f"""
<div class="kpi-card">
<div class="kpi-label">Revenue</div>
<div class="kpi-value">AED {total_revenue:,.0f}</div>
<div class="kpi-note">Selected segment</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with k2:
        st.markdown(
            f"""
<div class="kpi-card">
<div class="kpi-label">Orders</div>
<div class="kpi-value">{total_orders:,}</div>
<div class="kpi-note">Observed transactions</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with k3:
        st.markdown(
            f"""
<div class="kpi-card">
<div class="kpi-label">AOV</div>
<div class="kpi-value">AED {aov:,.2f}</div>
<div class="kpi-note">Revenue / orders</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with k4:
        st.markdown(
            f"""
<div class="kpi-card">
<div class="kpi-label">Conversion</div>
<div class="kpi-value">{conversion_rate:.2f}%</div>
<div class="kpi-note">Orders / sessions</div>
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns(
        [1.45, 1],
        gap="large",
    )

    with left:

        city_channel = (
            filtered_df
            .groupby(
                [
                    "city",
                    "acquisition_channel",
                ],
                as_index=False,
            )["revenue"]
            .sum()
        )

        fig = px.bar(
            city_channel,
            x="city",
            y="revenue",
            color="acquisition_channel",
            color_discrete_map=CHANNEL_COLORS,
            barmode="stack",
            title="Revenue distribution by market and acquisition channel",
            labels={
                "revenue": "Revenue (AED)",
                "city": "Market",
                "acquisition_channel": "Channel",
            },
        )

        fig = apply_plotly_theme(fig)

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with right:

        channel_orders = (
            filtered_df
            .groupby(
                "acquisition_channel",
                as_index=False,
            )["orders"]
            .sum()
        )

        fig = px.pie(
            channel_orders,
            names="acquisition_channel",
            values="orders",
            hole=0.62,
            color="acquisition_channel",
            color_discrete_map=CHANNEL_COLORS,
            title="Order contribution by acquisition channel",
        )

        fig = apply_plotly_theme(fig)

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    st.markdown(
        """
<div class="section-title">
Decision signals
</div>
""",
        unsafe_allow_html=True,
    )

    channel_summary = (
        filtered_df
        .groupby(
            "acquisition_channel",
            as_index=False,
        )
        .agg(
            revenue=("revenue", "sum"),
            orders=("orders", "sum"),
            sessions=("sessions", "sum"),
        )
    )

    channel_summary["conversion_rate"] = (
        channel_summary["orders"]
        /
        channel_summary["sessions"]
        * 100
    )

    if not channel_summary.empty:

        strongest_revenue = (
            channel_summary
            .sort_values(
                "revenue",
                ascending=False,
            )
            .iloc[0]
        )

        strongest_conversion = (
            channel_summary
            .sort_values(
                "conversion_rate",
                ascending=False,
            )
            .iloc[0]
        )

        st.markdown(
            f"""
<div class="insight">
<div class="insight-title">
Revenue concentration
</div>
<div class="insight-text">
<strong>{strongest_revenue['acquisition_channel']}</strong>
is currently the largest revenue contributor in the selected dataset,
with AED {strongest_revenue['revenue']:,.0f}.
</div>
</div>

<div class="insight">
<div class="insight-title">
Conversion opportunity
</div>
<div class="insight-text">
<strong>{strongest_conversion['acquisition_channel']}</strong>
shows the highest observed order-to-session conversion rate at
{strongest_conversion['conversion_rate']:.2f}%.
This should be investigated for transferable acquisition or
landing-page behaviours before increasing spend.
</div>
</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# 11. GROWTH DIAGNOSTICS
# ============================================================

elif page == "Growth Diagnostics":

    st.markdown(
        """
<div class="section-label">
02 / Growth Diagnostics
</div>

<div class="section-title">
Where is growth coming from?
</div>

<div class="section-description">
Diagnose revenue, volume and conversion performance across markets and channels.
</div>
""",
        unsafe_allow_html=True,
    )

    city_summary = (
        filtered_df
        .groupby(
            "city",
            as_index=False,
        )
        .agg(
            revenue=("revenue", "sum"),
            orders=("orders", "sum"),
            sessions=("sessions", "sum"),
        )
    )

    city_summary["conversion_rate"] = (
        city_summary["orders"]
        /
        city_summary["sessions"]
        * 100
    )

    city_summary["aov"] = (
        city_summary["revenue"]
        /
        city_summary["orders"]
    )

    c1, c2 = st.columns(2)

    with c1:

        fig = px.bar(
            city_summary.sort_values(
                "revenue",
                ascending=False,
            ),
            x="city",
            y="revenue",
            title="Revenue by market",
            labels={
                "revenue": "Revenue (AED)",
                "city": "Market",
            },
        )

        fig = apply_plotly_theme(fig)

        fig.update_traces(
            marker_color="#00D084"
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with c2:

        fig = px.scatter(
            city_summary,
            x="conversion_rate",
            y="aov",
            size="orders",
            color="city",
            title="Conversion vs. average order value",
            labels={
                "conversion_rate": "Conversion rate (%)",
                "aov": "Average order value (AED)",
                "city": "Market",
            },
        )

        fig = apply_plotly_theme(fig)

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    st.markdown(
        """
<div class="section-title">
Market diagnostic table
</div>
""",
        unsafe_allow_html=True,
    )

    display_city = city_summary.copy()

    display_city["revenue"] = (
        display_city["revenue"]
        .round(2)
    )

    display_city["aov"] = (
        display_city["aov"]
        .round(2)
    )

    display_city["conversion_rate"] = (
        display_city["conversion_rate"]
        .round(2)
    )

    st.dataframe(
        display_city,
        use_container_width=True,
        hide_index=True,
    )


# ============================================================
# 12. CUSTOMER FUNNEL
# ============================================================

elif page == "Customer Funnel":

    st.markdown(
        """
<div class="section-label">
03 / Customer Funnel
</div>

<div class="section-title">
Understanding customer movement
</div>

<div class="section-description">
A simplified funnel view connecting acquisition activity to orders and repeat behaviour.
</div>
""",
        unsafe_allow_html=True,
    )

    funnel_values = [
        total_sessions,
        new_users + returning_users,
        total_orders,
    ]

    funnel_labels = [
        "Sessions",
        "Active users represented",
        "Orders",
    ]

    fig = go.Figure(
        go.Funnel(
            y=funnel_labels,
            x=funnel_values,
            textinfo="value+percent initial",
            marker=dict(
                color=[
                    "#647080",
                    "#4DA3FF",
                    "#00D084",
                ]
            ),
        )
    )

    fig.update_layout(
        title="Acquisition-to-order funnel",
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(
            family="DM Sans",
            color=TEXT_COLOR,
        ),
        title_font=dict(
            family="Space Grotesk",
            size=18,
        ),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    f1, f2 = st.columns(2)

    with f1:

        st.markdown(
            f"""
<div class="premium-card">

<div class="card-kicker">
CUSTOMER MIX
</div>

<div class="card-title">
New vs. returning customers
</div>

<div class="card-text">
Returning users represent approximately
<strong>{retention_mix:.1f}%</strong>
of the user mix represented by the dataset.
This is a diagnostic indicator rather than a measured
Careem customer-retention rate.
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with f2:

        st.markdown(
            f"""
<div class="premium-card">

<div class="card-kicker">
ANALYTICAL QUESTION
</div>

<div class="card-title">
Where should retention investment focus?
</div>

<div class="card-text">
Compare acquisition channels by repeat-user contribution,
conversion rate and revenue per order before reallocating
growth investment.
The next analytical step would be cohort-level retention
and lifetime-value analysis using actual company data.
</div>

</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# 13. EXPERIMENTATION
# ============================================================

elif page == "Experimentation":

    st.markdown(
        """
<div class="section-label">
04 / Experimentation
</div>

<div class="section-title">
Turning diagnosis into action
</div>

<div class="section-description">
Illustrative experiments derived from the observed signals.
These are hypotheses, not claims about Careem's current strategy.
</div>
""",
        unsafe_allow_html=True,
    )

    experiments = [
        (
            "01",
            "Channel conversion experiment",
            "Test whether the strongest-converting acquisition channel can transfer its messaging, landing experience or audience structure to another high-volume channel.",
            "Primary KPI: conversion rate"
        ),
        (
            "02",
            "Order-value experiment",
            "Test basket-building mechanics such as bundles or threshold-based offers while monitoring incremental revenue and unit economics.",
            "Primary KPI: incremental contribution per order"
        ),
        (
            "03",
            "Retention experiment",
            "Create behavioural cohorts based on order frequency and recency, then test targeted re-engagement journeys against a control group.",
            "Primary KPI: repeat-order rate"
        ),
        (
            "04",
            "Market-specific experiment",
            "Compare high-conversion and high-revenue markets to identify transferable customer, merchant or operational characteristics.",
            "Primary KPI: revenue per active customer"
        ),
    ]

    for number, title, description, metric in experiments:

        st.markdown(
            f"""
<div class="premium-card">

<div class="card-kicker">
EXPERIMENT {number}
</div>

<div class="card-title">
{title}
</div>

<div class="card-text">
{description}
</div>

<div style="
    margin-top:0.8rem;
    font-family:'JetBrains Mono';
    font-size:0.65rem;
    color:#00D084;
">
{metric.upper()}
</div>

</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<br>",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
<div class="insight">
<div class="insight-title">
Experimentation principle
</div>
<div class="insight-text">
A growth decision should not be based only on correlation.
The recommended sequence is hypothesis → experiment → control →
measurement → interpretation → decision.
</div>
</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# 14. DATA EXPLORER
# ============================================================

elif page == "Data Explorer":

    st.markdown(
        """
<div class="section-label">
05 / Data Explorer
</div>

<div class="section-title">
Inspect the analytical layer
</div>

<div class="section-description">
Explore the records powering the dashboard and review calculated fields.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="premium-card">

<div class="card-kicker">
DATASET
</div>

<div class="card-title">
{DATA_MODE}
</div>

<div class="card-text">
Records currently loaded: <strong>{len(filtered_df):,}</strong>.
The dashboard recalculates the displayed metrics dynamically from
the selected records.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
    )

    csv = filtered_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Export filtered dataset",
        csv,
        "careem_growth_analysis_export.csv",
        "text/csv",
    )


# ============================================================
# 15. METHODOLOGY & SOURCES
# ============================================================

elif page == "Methodology & Sources":

    st.markdown(
        """
<div class="section-label">
06 / Methodology & Sources
</div>

<div class="section-title">
Evidence, assumptions and boundaries
</div>

<div class="section-description">
This section makes the analytical provenance explicit.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="premium-card">

<div class="card-kicker">
IMPORTANT DATA DISCLOSURE
</div>

<div class="card-title">
This is an independent analytical prototype.
</div>

<div class="card-text">
The dashboard is not an official Careem system and does not use
Careem confidential, proprietary or internal data.
When the local data.csv file is unavailable, the application generates
a synthetic dataset solely to demonstrate analytical methods,
dashboard design and decision-support logic.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="section-title">
Analytical framework
</div>
""",
        unsafe_allow_html=True,
    )

    framework = [
        (
            "01",
            "Ingestion",
            "Load structured operational or growth records."
        ),
        (
            "02",
            "Validation",
            "Check required fields, missing values and data consistency."
        ),
        (
            "03",
            "Aggregation",
            "Calculate revenue, orders, AOV, conversion and customer mix."
        ),
        (
            "04",
            "Diagnosis",
            "Compare markets, acquisition channels and funnel behaviour."
        ),
        (
            "05",
            "Storytelling",
            "Translate patterns into concise business questions and signals."
        ),
        (
            "06",
            "Action",
            "Convert evidence into testable hypotheses and experiments."
        ),
    ]

    for number, title, description in framework:

        st.markdown(
            f"""
<div class="source-item">

<div class="source-number">
STEP {number}
</div>

<div class="source-title">
{title}
</div>

<div class="source-description">
{description}
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
<div class="section-title" style="margin-top:2rem;">
References
</div>
""",
        unsafe_allow_html=True,
    )

    sources = [
        (
            "01",
            "Careem — About Us",
            "Official Careem corporate source used only for publicly stated company context such as Careem's Everything App positioning, geographic footprint and platform description.",
            "https://www.careem.com/en-AE/about-us/"
        ),
        (
            "02",
            "Careem — Food",
            "Official Careem Food source used for public product context, including Food's restaurant marketplace positioning and customer-facing service description.",
            "https://www.careem.com/en-AE/food/"
        ),
        (
            "03",
            "Careem — The Everything App",
            "Official Careem source used to understand the public structure of the wider Careem platform and its Go, Eat, Get and Pay service categories.",
            "https://www.careem.com/en-AE/"
        ),
        (
            "04",
            "Careem Engineering — Product Updates",
            "Official Careem Engineering source used for public product context around recent Food and app-navigation improvements.",
            "https://engineering.careem.com/"
        ),
        (
            "05",
            "Careem Growth Manager Job Description",
            "User-provided job description. Used to shape the analytical themes demonstrated in this prototype: growth planning, dashboards, funnel health, experimentation, customer segmentation, program management and business decision support.",
            ""
        ),
        (
            "06",
            "Anjalo Theophine Wilson — GitHub Repository",
            "Project repository containing the implementation of this independent portfolio prototype.",
            "https://github.com/theanjalo877-jpg/careem-auto-analyst"
        ),
    ]

    for number, title, description, url in sources:

        link_html = ""

        if url:
            link_html = f"""
<div style="
    margin-top:0.5rem;
    font-family:'JetBrains Mono';
    font-size:0.62rem;
    color:#647080;
">
SOURCE AVAILABLE IN APPLICATION
</div>
"""

        st.markdown(
            f"""
<div class="source-item">

<div class="source-number">
SOURCE {number}
</div>

<div class="source-title">
{title}
</div>

<div class="source-description">
{description}
</div>

{link_html}

</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="premium-card">

<div class="card-kicker">
SOURCE GOVERNANCE
</div>

<div class="card-title">
What is sourced vs. what is analytical?
</div>

<div class="card-text">

<strong>Publicly sourced:</strong>
Careem company and product context.

<br><br>

<strong>User-provided:</strong>
The Growth Manager job requirements used to frame the case-study
questions and analytical capabilities.

<br><br>

<strong>Independently created:</strong>
The dataset, calculations, visualisations, diagnostic logic,
experimentation hypotheses and recommendations in this prototype.

<br><br>

This separation prevents the prototype from presenting
synthetic analytical output as confidential Careem information.

</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# 16. FOOTER
# ============================================================

st.markdown(
    """
<br><br>

<div style="
    border-top:1px solid rgba(255,255,255,0.08);
    padding-top:1.5rem;
    text-align:center;
    color:#647080;
    font-family:'JetBrains Mono';
    font-size:0.62rem;
    letter-spacing:0.08em;
">

INDEPENDENT BUSINESS ANALYTICS PROTOTYPE
&nbsp; • &nbsp;
ANJALO THEOPHINE WILSON
&nbsp; • &nbsp;
2026

</div>
""",
    unsafe_allow_html=True,
)
