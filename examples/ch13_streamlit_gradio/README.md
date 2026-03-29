# Chapter 13 Examples: Streamlit & Gradio for Scientists

Three working examples demonstrating how to turn Python scripts into web applications that colleagues can use without coding.

## Setup

```bash
pip install streamlit gradio pandas numpy scipy matplotlib
```

## Examples

### 1. Data Explorer (Streamlit)
Upload any CSV, get instant statistics, plots, and hypothesis tests.

```bash
streamlit run 01_data_explorer.py
```

**Features:** Descriptive stats, missing value detection, histograms, scatter plots, box plots, correlation matrix, t-test, Mann-Whitney U, Pearson correlation, CSV download.

### 2. Equation Plotter (Gradio)
Enter any equation, adjust parameters with sliders, see the plot update live.

```bash
python 02_equation_solver.py
```

**Features:** Real-time equation plotting, parameter sliders, automatic zero-finding, preset examples (quadratic, Gaussian, damped sine, logistic, cubic).

### 3. Sensor Dashboard (Streamlit)
Real-time monitoring dashboard with alerts. Replace simulated data with your actual sensors.

```bash
streamlit run 03_sensor_dashboard.py
```

**Features:** KPI cards with deltas, configurable alert thresholds, time series charts, auto-refresh, CSV export. Ready to connect to real data sources (CSV, SQL, API, MQTT).

## Key Takeaway

Each of these apps took ~100 lines of Python. With AI coding assistants (Ch 5), you can describe what you want and have the assistant generate a Streamlit/Gradio app for your specific use case in minutes.
