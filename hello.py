from preswald import connect, get_df, text, table, plotly, query, slider
import plotly.express as px
import pandas as pd
import os

# 🔌 Connect to the dataset
connect()
df = get_df("air_pollution")

if df is None:
    text("❌ Dataset failed to load. Check your 'preswald.toml' or the file path.")
else:
    text("# 🌍 Global Air Pollution Dashboard")

    # ✅ Rename columns for SQL safety
    df.columns = [col.replace(" ", "_").replace(".", "_") for col in df.columns]

    # Show top 15 rows
    table(df.head(15), title="📄 Top 15 Rows Preview")
    text("🧩 Columns available: " + ", ".join(df.columns))

    # Detect PM2.5 column
    pm_col = next((col for col in df.columns if "PM2_5" in col), None)

    if "Country" in df.columns and pm_col:
        df[pm_col] = pd.to_numeric(df[pm_col], errors="coerce")
        df = df.dropna(subset=["Country", pm_col])

        # 📊 Summary
        summary = df.groupby("Country")[pm_col].agg(["mean", "max"]).reset_index()
        summary.columns = ["Country", "Average_PM2_5", "Max_PM2_5"]
        table(summary.sort_values("Average_PM2_5", ascending=False), title="📊 PM2.5 Summary by Country")

        # 📉 Bar Chart
        fig = px.histogram(df, x="Country", y=pm_col, color="Country", title="🌫️ PM2.5 Levels by Country")
        plotly(fig)

        # 📈 Yearly trend (optional)
        if "Year" in df.columns:
            df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
            yearwise = df.dropna(subset=["Year"]).groupby("Year")[pm_col].mean().reset_index()
            line = px.line(yearwise, x="Year", y=pm_col, title="📈 Year-wise PM2.5 Trend (Global Avg)")
            plotly(line)

        # 🗺️ Geo Map
        if {"Latitude", "Longitude"}.issubset(df.columns):
            df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
            df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
            df_map = df.dropna(subset=["Latitude", "Longitude"])
            map_fig = px.scatter_geo(
                df_map,
                lat="Latitude",
                lon="Longitude",
                color="Country",
                hover_name="City" if "City" in df.columns else "Country",
                title="🗺️ Global PM2.5 Data Points",
                projection="natural earth"
            )
            plotly(map_fig)

        # ✅ Save cleaned data for querying
        clean_path = "data/clean_air_pollution.csv"
        os.makedirs("data", exist_ok=True)
        df.to_csv(clean_path, index=False)

        # 🔍 SQL Query: High PM2.5 areas
        text("## 🔎 SQL Query Output: PM2.5 > 100")
        text(f"🧾 Query: SELECT * FROM clean_air_pollution WHERE `{pm_col}` > 100")
        sql_result = query(f"SELECT * FROM clean_air_pollution WHERE `{pm_col}` > 100", "clean_air_pollution")
        if sql_result is not None and not sql_result.empty:
            table(sql_result.head(10), title="📋 Cities with PM2.5 > 100")
        else:
            text("⚠️ No records found for PM2.5 > 100. Try lowering the threshold.")

        # 🎛️ Slider-based dynamic filter
        text("## 🎚️ Adjust PM2.5 Threshold (Dynamic Filter)")
        threshold = slider("Select PM2.5 Threshold", min_val=0, max_val=300, default=50)
        filtered = df[df[pm_col] > threshold]
        table(filtered.head(20), title=f"📌 Cities with PM2.5 > {threshold}")

        # 📍 City-wise scatter
        if "City" in df.columns:
            scatter = px.scatter(df, x="City", y=pm_col, color="Country", title="🏙️ PM2.5 Levels by City & Country")
            plotly(scatter)

    else:
        text("⚠️ Required columns 'Country' or 'PM2.5' not found. Columns available: " + ", ".join(df.columns))
