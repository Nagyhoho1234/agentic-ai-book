"""
Streamlit Data Explorer for Scientists
=======================================
Upload a CSV, explore it visually, run basic statistics.
No coding required to USE this app — just run: streamlit run 01_data_explorer.py

This example demonstrates how a scientist can share an analysis tool
with colleagues who have zero programming experience.
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Scientific Data Explorer", layout="wide")
st.title("Scientific Data Explorer")
st.markdown("Upload your CSV data and explore it — no coding required.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv", "txt"])

if uploaded_file is not None:
    # Try common separators
    sep = st.sidebar.selectbox("Separator", [",", ";", "\t", " "], index=0)
    df = pd.read_csv(uploaded_file, sep=sep)

    st.subheader(f"Dataset: {uploaded_file.name}")
    st.write(f"**{df.shape[0]} rows × {df.shape[1]} columns**")

    # --- Data Preview ---
    with st.expander("Preview Data", expanded=True):
        st.dataframe(df.head(50), use_container_width=True)

    # --- Column Types ---
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

    st.sidebar.header("Column Info")
    st.sidebar.write(f"Numeric: {len(numeric_cols)}")
    st.sidebar.write(f"Categorical: {len(categorical_cols)}")

    # --- Descriptive Statistics ---
    st.subheader("Descriptive Statistics")
    if numeric_cols:
        st.dataframe(df[numeric_cols].describe().round(4), use_container_width=True)
    else:
        st.warning("No numeric columns found.")

    # --- Missing Values ---
    missing = df.isnull().sum()
    if missing.sum() > 0:
        st.subheader("Missing Values")
        st.dataframe(missing[missing > 0].rename("Count"), use_container_width=True)

    # --- Visualization ---
    if numeric_cols:
        st.subheader("Quick Visualization")
        col1, col2 = st.columns(2)

        with col1:
            plot_type = st.selectbox("Plot type", ["Histogram", "Scatter", "Box Plot", "Line"])
        with col2:
            x_col = st.selectbox("X axis", numeric_cols, index=0)

        if plot_type == "Histogram":
            bins = st.slider("Bins", 5, 100, 30)
            st.bar_chart(df[x_col].value_counts(bins=bins).sort_index())

        elif plot_type == "Scatter":
            y_col = st.selectbox("Y axis", numeric_cols, index=min(1, len(numeric_cols) - 1))
            st.scatter_chart(df, x=x_col, y=y_col)

        elif plot_type == "Box Plot":
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            df[numeric_cols].boxplot(ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)

        elif plot_type == "Line":
            st.line_chart(df[x_col])

    # --- Correlation Matrix ---
    if len(numeric_cols) >= 2:
        st.subheader("Correlation Matrix")
        corr = df[numeric_cols].corr().round(3)
        st.dataframe(corr.style.background_gradient(cmap="RdBu_r", vmin=-1, vmax=1),
                     use_container_width=True)

    # --- Simple Hypothesis Test ---
    if len(numeric_cols) >= 2:
        st.subheader("Quick Hypothesis Test")
        from scipy import stats
        col_a = st.selectbox("Group A", numeric_cols, index=0, key="ha")
        col_b = st.selectbox("Group B", numeric_cols, index=min(1, len(numeric_cols) - 1), key="hb")

        data_a = df[col_a].dropna()
        data_b = df[col_b].dropna()

        test_type = st.radio("Test", ["t-test (independent)", "Mann-Whitney U", "Pearson correlation"])

        if test_type == "t-test (independent)":
            stat, p = stats.ttest_ind(data_a, data_b)
            st.write(f"t-statistic: **{stat:.4f}**, p-value: **{p:.4e}**")
        elif test_type == "Mann-Whitney U":
            stat, p = stats.mannwhitneyu(data_a, data_b)
            st.write(f"U-statistic: **{stat:.4f}**, p-value: **{p:.4e}**")
        elif test_type == "Pearson correlation":
            r, p = stats.pearsonr(data_a, data_b)
            st.write(f"r: **{r:.4f}**, p-value: **{p:.4e}**")

        if p < 0.05:
            st.success(f"Statistically significant (p = {p:.4e} < 0.05)")
        else:
            st.info(f"Not statistically significant (p = {p:.4e} >= 0.05)")

    # --- Download Processed Data ---
    st.subheader("Download")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download processed CSV", csv, "processed_data.csv", "text/csv")

else:
    st.info("Upload a CSV file to get started. Try any dataset from your research!")
    st.markdown("""
    **What this app does:**
    - Shows descriptive statistics for all numeric columns
    - Detects missing values
    - Creates histograms, scatter plots, box plots, and line charts
    - Computes correlation matrices
    - Runs t-tests, Mann-Whitney U, and Pearson correlation
    - Lets you download the processed data

    **How to share with colleagues:**
    ```
    pip install streamlit pandas scipy matplotlib
    streamlit run 01_data_explorer.py
    ```
    Then send them the URL that appears in the terminal.
    """)
