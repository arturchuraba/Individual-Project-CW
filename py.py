# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "pandas",
#     "plotly",
#     "numpy",
# ]
# ///

import marimo

__generated_with__ = "0.23.1"
app = marimo.App()

@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    import numpy as np
    return go, mo, np, pd, px

@app.cell
def __(mo):
    # Tab 1: About Me - Artur Churaba Portfolio
    tab_about = mo.vstack([
        mo.md("""
        # Artur Churaba

        ### BSc Accounting & Finance | Bayes Business School

        ---

        ## 👋 About Me

        I work with datasets and visualize them to make it easier and more clear to read. This portfolio demonstrates my ability to work with data, build interactive tools, and present findings effectively.

        ## 🎓 Education

        **BSc Accounting & Finance** | Bayes Business School (2025 – Present)
        - Introduction to Data Science and AI Tools
        - Financial Accounting

        ## 🛠️ Technical Skills

        ### Programming & Data Analysis
        - **Python** (Pandas, NumPy, Plotly, Marimo) — Data manipulation and visualization
        - **Interactive Dashboards** — Building dynamic, filterable web apps
        - **Data Filtering & UI Controls** — Dropdowns, sliders, and interactive tables

        ### Financial Analysis
        - **Altman Z-Score Modelling** — Bankruptcy risk prediction
        - **Financial Data Interpretation** — Analyzing S&P 500 company metrics
        - **Cost of Debt Analysis** — Understanding credit risk impact on borrowing costs
        - **Panel Data Analysis** — Multi-year trends (2020-2024)

        ### Tools & Technologies
        - **Version Control** — Git, GitHub Codespaces
        - **Data Visualization** — Plotly, Marimo UI components
        - **Data Processing** — Pandas, NumPy

        ## 📊 What This Portfolio Shows

        - **Data-Driven Risk & Cost Analysis** — Z-Score vs Cost of Debt relationships
        - **Interactive Filtering** — Filter by sector and market cap
        - **S&P 500 Analysis** — Real company financial data
        - **Panel Data Trends** — Multi-year financial analysis (2020-2024)

        ---
        *This portfolio demonstrates my data science and financial analysis capabilities.*
        """)
    ])
    return (tab_about,)

@app.cell
def __(np, pd, px):
    # Tab 2: S&P 500 Z-Score vs Cost of Debt Analysis
    
    # Sector colors for consistent visualization
    sector_colors = {
        'consumer-cyclical': '#3498db',
        'energy': '#e67e22',
        'communication-services': '#27ae60',
        'basic-materials': '#e74c3c',
        'healthcare': '#9b59b6',
        'technology': '#1abc9c',
        'industrials': '#f39c12',
        'financials': '#2980b9',
    }
    
    # S&P 500 sample data
    sp500_data = [
        {'ticker': 'AAPL', 'name': 'Apple Inc.', 'sector': 'technology', 'zscore': 14.2, 'cod': 1.0, 'mktcap': 2380},
        {'ticker': 'MSFT', 'name': 'Microsoft Corp.', 'sector': 'technology', 'zscore': 16.8, 'cod': 0.9, 'mktcap': 1790},
        {'ticker': 'GOOGL', 'name': 'Alphabet Inc.', 'sector': 'communication-services', 'zscore': 18.4, 'cod': 0.6, 'mktcap': 1140},
        {'ticker': 'AMZN', 'name': 'Amazon.com Inc.', 'sector': 'consumer-cyclical', 'zscore': 3.8, 'cod': 2.1, 'mktcap': 860},
        {'ticker': 'NVDA', 'name': 'NVIDIA Corp.', 'sector': 'technology', 'zscore': 19.3, 'cod': 0.8, 'mktcap': 360},
        {'ticker': 'META', 'name': 'Meta Platforms Inc.', 'sector': 'communication-services', 'zscore': 14.7, 'cod': 0.7, 'mktcap': 319},
        {'ticker': 'UNH', 'name': 'UnitedHealth Group Inc.', 'sector': 'healthcare', 'zscore': 4.6, 'cod': 1.8, 'mktcap': 489},
        {'ticker': 'JNJ', 'name': 'Johnson & Johnson', 'sector': 'healthcare', 'zscore': 5.9, 'cod': 1.4, 'mktcap': 434},
        {'ticker': 'V', 'name': 'Visa Inc.', 'sector': 'financials', 'zscore': 13.5, 'cod': 0.9, 'mktcap': 437},
        {'ticker': 'XOM', 'name': 'Exxon Mobil Corp.', 'sector': 'energy', 'zscore': 2.4, 'cod': 3.1, 'mktcap': 443},
        {'ticker': 'JPM', 'name': 'JPMorgan Chase & Co.', 'sector': 'financials', 'zscore': 1.8, 'cod': 2.7, 'mktcap': 399},
        {'ticker': 'WMT', 'name': 'Walmart Inc.', 'sector': 'consumer-cyclical', 'zscore': 3.2, 'cod': 2.3, 'mktcap': 386},
        {'ticker': 'PG', 'name': 'Procter & Gamble Co.', 'sector': 'consumer-cyclical', 'zscore': 3.5, 'cod': 2.1, 'mktcap': 356},
        {'ticker': 'CVX', 'name': 'Chevron Corp.', 'sector': 'energy', 'zscore': 2.6, 'cod': 2.9, 'mktcap': 340},
        {'ticker': 'HD', 'name': 'Home Depot Inc.', 'sector': 'consumer-cyclical', 'zscore': 2.0, 'cod': 3.4, 'mktcap': 298},
        {'ticker': 'KO', 'name': 'Coca-Cola Co.', 'sector': 'consumer-cyclical', 'zscore': 2.5, 'cod': 2.8, 'mktcap': 268},
        {'ticker': 'PEP', 'name': 'PepsiCo Inc.', 'sector': 'consumer-cyclical', 'zscore': 3.0, 'cod': 2.6, 'mktcap': 244},
        {'ticker': 'TXN', 'name': 'Texas Instruments Inc.', 'sector': 'technology', 'zscore': 7.4, 'cod': 1.5, 'mktcap': 163},
        {'ticker': 'NFLX', 'name': 'Netflix Inc.', 'sector': 'communication-services', 'zscore': 3.6, 'cod': 2.3, 'mktcap': 123},
        {'ticker': 'INTC', 'name': 'Intel Corp.', 'sector': 'technology', 'zscore': 4.5, 'cod': 2.0, 'mktcap': 116},
        {'ticker': 'CSCO', 'name': 'Cisco Systems Inc.', 'sector': 'technology', 'zscore': 9.1, 'cod': 1.3, 'mktcap': 195},
        {'ticker': 'DIS', 'name': 'Walt Disney Co.', 'sector': 'communication-services', 'zscore': 1.9, 'cod': 3.5, 'mktcap': 181},
        {'ticker': 'VZ', 'name': 'Verizon Communications Inc.', 'sector': 'communication-services', 'zscore': 1.4, 'cod': 4.2, 'mktcap': 170},
        {'ticker': 'WFC', 'name': 'Wells Fargo & Co.', 'sector': 'financials', 'zscore': 1.6, 'cod': 3.0, 'mktcap': 172},
        {'ticker': 'GS', 'name': 'Goldman Sachs Group Inc.', 'sector': 'financials', 'zscore': 1.7, 'cod': 3.2, 'mktcap': 123},
        {'ticker': 'CAT', 'name': 'Caterpillar Inc.', 'sector': 'industrials', 'zscore': 3.2, 'cod': 2.4, 'mktcap': 118},
        {'ticker': 'GE', 'name': 'General Electric Co.', 'sector': 'industrials', 'zscore': 1.6, 'cod': 3.9, 'mktcap': 94},
        {'ticker': 'PFE', 'name': 'Pfizer Inc.', 'sector': 'healthcare', 'zscore': 4.2, 'cod': 1.8, 'mktcap': 276},
        {'ticker': 'MRK', 'name': 'Merck & Co. Inc.', 'sector': 'healthcare', 'zscore': 3.3, 'cod': 2.2, 'mktcap': 275},
        {'ticker': 'MCD', 'name': "McDonald's Corp.", 'sector': 'consumer-cyclical', 'zscore': 1.2, 'cod': 4.3, 'mktcap': 207},
        {'ticker': 'SBUX', 'name': 'Starbucks Corp.', 'sector': 'consumer-cyclical', 'zscore': 1.5, 'cod': 4.1, 'mktcap': 104},
        {'ticker': 'NKE', 'name': 'Nike Inc.', 'sector': 'consumer-cyclical', 'zscore': 6.2, 'cod': 1.6, 'mktcap': 167},
        {'ticker': 'LIN', 'name': 'Linde PLC', 'sector': 'basic-materials', 'zscore': 4.1, 'cod': 1.9, 'mktcap': 153},
        {'ticker': 'MA', 'name': 'Mastercard Inc.', 'sector': 'financials', 'zscore': 11.2, 'cod': 1.0, 'mktcap': 339},
        {'ticker': 'ORCL', 'name': 'Oracle Corp.', 'sector': 'technology', 'zscore': 2.1, 'cod': 3.6, 'mktcap': 216},
    ]
    
    df_sp500 = pd.DataFrame(sp500_data)
    
    # Add risk category based on Z-Score
    df_sp500['risk_category'] = df_sp500['zscore'].apply(
        lambda x: 'High Risk (Distress)' if x < 1.81 else ('Medium Risk (Grey)' if x <= 2.99 else 'Low Risk (Safe)')
    )
    
    # Get unique sectors for filter
    sectors = ['All'] + sorted(df_sp500['sector'].unique().tolist())
    
    # Create UI filters
    sector_filter = mo.ui.dropdown(
        options=sectors,
        value='All',
        label="Filter by Sector"
    )
    
    mktcap_slider = mo.ui.slider(
        start=0,
        stop=2500,
        step=50,
        value=0,
        label="Minimum Market Cap ($B)"
    )
    
    # Summary by risk category
    risk_summary = df_sp500.groupby('risk_category').agg({
        'ticker': 'count',
        'cod': 'mean',
        'zscore': 'mean',
        'mktcap': 'mean'
    }).round(2).reset_index()
    risk_summary.columns = ['Risk Category', 'Number of Companies', 'Avg Cost of Debt (%)', 'Avg Z-Score', 'Avg Market Cap ($B)']
    
    # Panel Data (2020-2024)
    years = [2020, 2021, 2022, 2023, 2024]
    panel_data = []
    
    for year in years:
        for company in sp500_data[:20]:
            year_effect = (year - 2022) * 0.15
            panel_data.append({
                'ticker': company['ticker'],
                'sector': company['sector'],
                'year': year,
                'zscore': round(company['zscore'] + year_effect, 2),
                'cod': round(company['cod'] - year_effect * 0.4, 2),
            })
    
    df_panel = pd.DataFrame(panel_data)
    
    # Cost of Debt trend chart
    cost_trend = df_panel.groupby(['sector', 'year'])['cod'].mean().reset_index()
    fig_trend = px.line(cost_trend, x='year', y='cod', color='sector',
                         title='Cost of Debt Trends (2020-2024)',
                         labels={'year': 'Year', 'cod': 'Cost of Debt (%)'},
                         color_discrete_map=sector_colors)
    
    # Z-Score trend chart
    zscore_trend = df_panel.groupby(['sector', 'year'])['zscore'].mean().reset_index()
    fig_zscore = px.line(zscore_trend, x='year', y='zscore', color='sector',
                          title='Altman Z-Score Trends (2020-2024)',
                          labels={'year': 'Year', 'zscore': 'Z-Score'},
                          color_discrete_map=sector_colors)
    fig_zscore.add_hline(y=1.81, line_dash="dash", line_color="red", annotation_text="Distress")
    fig_zscore.add_hline(y=2.99, line_dash="dash", line_color="green", annotation_text="Safe")
    
    return (df_panel, df_sp500, fig_trend, fig_zscore, mktcap_slider, risk_summary, sector_colors, sector_filter, sp500_data)

@app.cell
def __(df_sp500, fig_trend, fig_zscore, mktcap_slider, px, sector_colors, sector_filter):
    # Cell 3: Filtered data and visualizations
    
    def get_filtered_data():
        filtered = df_sp500.copy()
        if sector_filter.value != 'All':
            filtered = filtered[filtered['sector'] == sector_filter.value]
        filtered = filtered[filtered['mktcap'] >= mktcap_slider.value]
        return filtered
    
    filtered_df = get_filtered_data()
    
    # Z-Score vs Cost of Debt Scatter Plot
    fig_scatter = px.scatter(
        filtered_df,
        x='zscore',
        y='cod',
        color='sector',
        size='mktcap',
        hover_name='ticker',
        text='ticker',
        title='Cost of Debt vs. Altman Z-Score (S&P 500, 2022)',
        labels={'zscore': 'Altman Z-Score', 'cod': 'Cost of Debt (%)', 'sector': 'Sector'},
        color_discrete_map=sector_colors
    )
    
    fig_scatter.add_vline(x=1.81, line_dash="dash", line_color="red", 
                           annotation_text="Distress (Z < 1.81)")
    fig_scatter.add_vline(x=2.99, line_dash="dash", line_color="green",
                           annotation_text="Safe (Z > 2.99)")
    fig_scatter.update_traces(textposition='top center', textfont_size=9)
    
    # Bar chart
    avg_by_sector = filtered_df.groupby('sector')['cod'].mean().reset_index()
    fig_bar = px.bar(
        avg_by_sector,
        x='sector',
        y='cod',
        color='sector',
        title='Average Cost of Debt by Sector',
        labels={'sector': 'Sector', 'cod': 'Avg Cost of Debt (%)'},
        color_discrete_map=sector_colors
    )
    
    # Histogram
    fig_hist = px.histogram(
        filtered_df,
        x='zscore',
        nbins=20,
        title='Altman Z-Score Distribution',
        labels={'zscore': 'Z-Score', 'count': 'Number of Companies'},
        color_discrete_sequence=['#1e3d6e']
    )
    fig_hist.add_vline(x=1.81, line_dash="dash", line_color="red")
    fig_hist.add_vline(x=2.99, line_dash="dash", line_color="green")
    
    return (avg_by_sector, fig_bar, fig_hist, fig_scatter, filtered_df)

@app.cell
def __(fig_bar, fig_hist, fig_scatter, fig_trend, fig_zscore, filtered_df, mo, mktcap_slider, risk_summary, sector_filter):
    # Cell 4: Dashboard layout
    
    data_table = mo.ui.table(
        filtered_df[['ticker', 'name', 'sector', 'zscore', 'cod', 'mktcap', 'risk_category']],
        label="S&P 500 Company Data"
    )
    
    high_risk_df = filtered_df[filtered_df['risk_category'] == 'High Risk (Distress)']
    low_risk_df = filtered_df[filtered_df['risk_category'] == 'Low Risk (Safe)']
    
    high_risk_avg = high_risk_df['cod'].mean() if len(high_risk_df) > 0 else 'N/A'
    low_risk_avg = low_risk_df['cod'].mean() if len(low_risk_df) > 0 else 'N/A'
    
    tab_dashboard = mo.vstack([
        mo.md("## 📊 Data-Driven Risk & Cost Analysis Dashboard"),
        mo.md("Use the filters to adjust sector selection and minimum market cap."),
        mo.md("---"),
        
        mo.md("### 🔧 Filters"),
        mo.hstack([sector_filter, mktcap_slider], justify="start", gap=2),
        
        mo.md("### 📈 Cost of Debt vs. Altman Z-Score"),
        mo.ui.plotly(fig_scatter),
        
        mo.md("### 📊 Average Cost of Debt by Sector"),
        mo.ui.plotly(fig_bar),
        
        mo.md("### 📉 Z-Score Distribution"),
        mo.ui.plotly(fig_hist),
        
        mo.md(f"""
        ### 📐 Key Statistical Insights
        
        | Metric | Value | Interpretation |
        |--------|-------|----------------|
        | **Correlation** | {filtered_df['zscore'].corr(filtered_df['cod']):.2f} | Negative correlation |
        | **Avg Cost of Debt (High Risk)** | {high_risk_avg}% | Higher borrowing costs |
        | **Avg Cost of Debt (Low Risk)** | {low_risk_avg}% | Lower borrowing costs |
        
        ### 🏢 Risk Category Summary
        """),
        
        mo.ui.table(risk_summary),
        
        mo.md("### 📈 Panel Data: 5-Year Trends (2020-2024)"),
        mo.md("Cost of Debt trends across sectors over time."),
        mo.ui.plotly(fig_trend),
        
        mo.md("### 📉 Altman Z-Score Trends (2020-2024)"),
        mo.ui.plotly(fig_zscore),
        
        mo.md("### 📋 Full Dataset"),
        data_table,
    ])
    
    return (data_table, tab_dashboard)

@app.cell
def __(mo, np, pd, px):
    # Tab 3: My Journey & Interests (Travel & Photography)
    
    # Travel data - with Rio de Janeiro 2026
    travel_data = [
        {'country': 'France', 'city': 'Paris', 'year': 2021, 'lat': 48.8566, 'lng': 2.3522},
        {'country': 'Italy', 'city': 'Rome', 'year': 2022, 'lat': 41.9028, 'lng': 12.4964},
        {'country': 'Spain', 'city': 'Barcelona', 'year': 2023, 'lat': 41.3851, 'lng': 2.1734},
        {'country': 'Japan', 'city': 'Tokyo', 'year': 2024, 'lat': 35.6762, 'lng': 139.6503},
        {'country': 'Turkey', 'city': 'Alanya', 'year': 2025, 'lat': 36.5442, 'lng': 31.9956},
        {'country': 'Spain', 'city': 'Mallorca', 'year': 2025, 'lat': 39.6953, 'lng': 3.0176},
        {'country': 'Brazil', 'city': 'Rio de Janeiro', 'year': 2026, 'lat': -22.9068, 'lng': -43.1729},
    ]
    
    df_travel = pd.DataFrame(travel_data)
    
    # Create year filter
    travel_year_filter = mo.ui.dropdown(
        options=[2021, 2022, 2023, 2024, 2025, 2026],
        value=2026,
        label="Select Year"
    )
    
    # Travel table
    travel_table = mo.ui.table(df_travel, label="My Complete Travel History")
    
    # Mini map showing ALL destinations
    all_destinations_map = px.scatter_mapbox(
        df_travel,
        lat='lat',
        lon='lng',
        hover_name='city',
        hover_data={'country': True, 'year': True},
        color='year',
        size=[12] * len(df_travel),
        title='🌍 All Travel Destinations (2021-2026)',
        zoom=1,
        height=400,
        size_max=15,
        color_continuous_scale='Viridis'
    )
    all_destinations_map.update_layout(mapbox_style="carto-positron")
    all_destinations_map.update_layout(margin=dict(l=0, r=0, t=50, b=0))
    
    tab_interests = mo.vstack([
        mo.md("""
        ## 🌍 My Hobbies: Travel & Photography

        When I'm not analyzing company financials, I love exploring the world and capturing moments through my camera lens.

        ---
        """),
        
        mo.md("### 🗺️ All Travel Destinations (Mini Map)"),
        mo.md("*This map shows ALL my travel destinations from 2021 to 2026, color-coded by year.*"),
        mo.ui.plotly(all_destinations_map),
        
        mo.md("---"),
        
        mo.md("### ✈️ Filter by Year"),
        mo.md("Select a specific year to see detailed destination information:"),
        travel_year_filter,
        
        mo.md("### 📅 Complete Travel History"),
        travel_table,
        
        mo.md("""
        ---
        ### 📸 Photography Portfolio
        
        I enjoy capturing:
        - **Landscape** — Mountains, coastlines, sunsets
        - **Street Photography** — Candid moments, urban architecture
        - **Travel** — Cultural events, local life
        
        ### 🎯 2026 Plans: Rio de Janeiro, Brazil 🇧🇷
        
        **Highlights I'm excited about:**
        - Christ the Redeemer statue
        - Copacabana and Ipanema beaches
        - Sugarloaf Mountain cable car
        - Samba music and Carnival culture
        - Fresh açaí and Brazilian cuisine
        """)
    ])
    
    return (tab_interests, travel_year_filter, df_travel, all_destinations_map)

@app.cell
def __(df_travel, mo, px, travel_year_filter):
    # Cell 5: Travel Map (separate cell to avoid UI element value access error)
    
    # Filter travel data based on selected year
    filtered_travel = df_travel[df_travel['year'] == travel_year_filter.value]
    
    # Create detailed map for selected year
    if len(filtered_travel) > 0:
        travel_map = px.scatter_mapbox(
            filtered_travel,
            lat='lat',
            lon='lng',
            hover_name='city',
            hover_data={'country': True, 'year': True},
            size=[20] * len(filtered_travel),
            title=f'📍 Travel Destinations in {travel_year_filter.value}',
            zoom=4,
            height=450,
            size_max=25
        )
        travel_map.update_layout(mapbox_style="carto-positron")
        travel_map.update_layout(margin=dict(l=0, r=0, t=50, b=0))
        travel_map_display = mo.ui.plotly(travel_map)
    else:
        travel_map_display = mo.md(f"✈️ No travel data recorded for {travel_year_filter.value}. Check back for updates!")
    
    # Display the map
    travel_map_display

@app.cell
def __(mo, tab_about, tab_dashboard, tab_interests, travel_map_display, travel_table, travel_year_filter, all_destinations_map):
    # Cell 6: Main Portfolio - 3 Tabs
    
    # Update interests tab with the map
    updated_tab_interests = mo.vstack([
        mo.md("""
        ## 🌍 My Hobbies: Travel & Photography

        When I'm not analyzing company financials, I love exploring the world and capturing moments through my camera lens.

        ---
        """),
        
        mo.md("### 🗺️ All Travel Destinations (Mini Map)"),
        mo.md("*This map shows ALL my travel destinations from 2021 to 2026, color-coded by year.*"),
        mo.ui.plotly(all_destinations_map),
        
        mo.md("---"),
        
        mo.md("### ✈️ Filter by Year"),
        mo.md("Select a specific year to see detailed destination information:"),
        travel_year_filter,
        
        mo.md("### 📍 Destinations Map for Selected Year"),
        travel_map_display,
        
        mo.md("### 📅 Complete Travel History"),
        travel_table,
        
        mo.md("""
        ---
        ### 📸 Photography Portfolio
        
        I enjoy capturing:
        - **Landscape** — Mountains, coastlines, sunsets
        - **Street Photography** — Candid moments, urban architecture
        - **Travel** — Cultural events, local life
        
        ### 🎯 2026 Plans: Rio de Janeiro, Brazil 🇧🇷
        
        **Highlights I'm excited about:**
        - Christ the Redeemer statue
        - Copacabana and Ipanema beaches
        - Sugarloaf Mountain cable car
        - Samba music and Carnival culture
        - Fresh açaí and Brazilian cuisine
        """)
    ])
    
    tabs = mo.ui.tabs({
        "📄 About Me": tab_about,
        "📊 Z-Score Dashboard": tab_dashboard,
        "✈️ My Journey & Interests": updated_tab_interests,
    })
    
    final_output = mo.vstack([
        mo.md("# Artur Churaba - Data Science Portfolio"),
        mo.md("### Bayes Business School | BSc Accounting & Finance"),
        mo.md("---"),
        mo.md("**Welcome to my portfolio!** This interactive dashboard demonstrates my data science and financial analysis capabilities."),
        mo.md(""),
        mo.md("### What You'll Find Here:"),
        mo.md("1. **About Me** - Education and skills"),
        mo.md("2. **Z-Score Dashboard** - Risk analysis with filters + 5-year trends"),
        mo.md("3. **My Journey & Interests** - Travel map and photography hobby"),
        mo.md(""),
        tabs,
        mo.md("---"),
        mo.md("*This portfolio demonstrates my data science and financial analysis capabilities.*")
    ])
    
    final_output

if __name__ == "__main__":
    app.run()