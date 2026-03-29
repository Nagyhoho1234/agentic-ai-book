"""
Streamlit Sensor Data Dashboard
================================
Simulates a real-time sensor monitoring dashboard.
In practice, replace the simulated data with your actual sensor feed.
Run: streamlit run 03_sensor_dashboard.py

Demonstrates how to build a lab monitoring dashboard that updates
automatically — useful for environmental monitoring, lab equipment,
field stations, or industrial processes.
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time


st.set_page_config(page_title="Sensor Dashboard", layout="wide")
st.title("Real-Time Sensor Monitoring Dashboard")


# --- Simulate sensor data (replace with real data source) ---
@st.cache_data(ttl=5)  # Refresh every 5 seconds
def get_sensor_data(n_points=200):
    """
    Simulates sensor data. In practice, replace this with:
    - pd.read_csv("latest_sensor_data.csv")
    - pd.read_sql("SELECT * FROM sensor_readings ORDER BY timestamp DESC LIMIT 200", conn)
    - requests.get("https://your-api/sensors/latest").json()
    - paho.mqtt.client for MQTT sensor streams
    """
    now = datetime.now()
    timestamps = [now - timedelta(minutes=i) for i in range(n_points, 0, -1)]

    np.random.seed(int(time.time()) // 10)  # Changes every 10 seconds
    base_temp = 22 + 3 * np.sin(np.linspace(0, 4 * np.pi, n_points))
    base_humidity = 55 + 10 * np.cos(np.linspace(0, 2 * np.pi, n_points))
    base_pressure = 1013 + 5 * np.sin(np.linspace(0, np.pi, n_points))

    return pd.DataFrame({
        "timestamp": timestamps,
        "temperature_C": base_temp + np.random.normal(0, 0.5, n_points),
        "humidity_pct": np.clip(base_humidity + np.random.normal(0, 2, n_points), 0, 100),
        "pressure_hPa": base_pressure + np.random.normal(0, 0.3, n_points),
        "CO2_ppm": 400 + np.cumsum(np.random.normal(0, 2, n_points)),
    })


# --- Configuration ---
st.sidebar.header("Settings")
refresh_rate = st.sidebar.selectbox("Refresh interval", [5, 10, 30, 60], index=1)
alert_temp = st.sidebar.slider("Temperature alert threshold (°C)", 15.0, 35.0, 28.0)
alert_humidity = st.sidebar.slider("Humidity alert threshold (%)", 30.0, 90.0, 75.0)
show_raw = st.sidebar.checkbox("Show raw data table", False)

# --- Get data ---
df = get_sensor_data()

# --- Current Values (KPI cards) ---
st.subheader("Current Readings")
col1, col2, col3, col4 = st.columns(4)

latest = df.iloc[-1]
prev = df.iloc[-2]

col1.metric("Temperature",
            f"{latest['temperature_C']:.1f} °C",
            f"{latest['temperature_C'] - prev['temperature_C']:.2f} °C")

col2.metric("Humidity",
            f"{latest['humidity_pct']:.1f} %",
            f"{latest['humidity_pct'] - prev['humidity_pct']:.2f} %")

col3.metric("Pressure",
            f"{latest['pressure_hPa']:.1f} hPa",
            f"{latest['pressure_hPa'] - prev['pressure_hPa']:.2f} hPa")

col4.metric("CO₂",
            f"{latest['CO2_ppm']:.0f} ppm",
            f"{latest['CO2_ppm'] - prev['CO2_ppm']:.1f} ppm")

# --- Alerts ---
alerts = []
if latest["temperature_C"] > alert_temp:
    alerts.append(f"Temperature ({latest['temperature_C']:.1f}°C) exceeds threshold ({alert_temp}°C)")
if latest["humidity_pct"] > alert_humidity:
    alerts.append(f"Humidity ({latest['humidity_pct']:.1f}%) exceeds threshold ({alert_humidity}%)")

if alerts:
    for alert in alerts:
        st.error(f"ALERT: {alert}")
else:
    st.success("All readings within normal range.")

# --- Time Series Charts ---
st.subheader("Time Series")

tab1, tab2, tab3, tab4 = st.tabs(["Temperature", "Humidity", "Pressure", "CO₂"])

with tab1:
    st.line_chart(df.set_index("timestamp")["temperature_C"])
with tab2:
    st.line_chart(df.set_index("timestamp")["humidity_pct"])
with tab3:
    st.line_chart(df.set_index("timestamp")["pressure_hPa"])
with tab4:
    st.line_chart(df.set_index("timestamp")["CO2_ppm"])

# --- Statistics ---
st.subheader("Summary Statistics (last 200 readings)")
stats = df[["temperature_C", "humidity_pct", "pressure_hPa", "CO2_ppm"]].describe().round(2)
st.dataframe(stats, use_container_width=True)

# --- Raw Data ---
if show_raw:
    st.subheader("Raw Data")
    st.dataframe(df, use_container_width=True)

# --- Download ---
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download sensor data as CSV", csv,
                   f"sensor_data_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                   "text/csv")

# --- Auto-refresh ---
st.markdown(f"*Auto-refreshes every {refresh_rate} seconds. "
            f"Last update: {datetime.now().strftime('%H:%M:%S')}*")
