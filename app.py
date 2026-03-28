import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Import your custom modules
from analyzer import get_summary, get_insights # (Your Groq/AI logic)
from visualizer import plot_sales_by_product, plot_sales_by_region

# --- Page Config ---
st.set_page_config(page_title="AI Data Agent", layout="wide")

st.title("AI Data Analysis Agent")
st.markdown("Analyzing your SQLite database with Groq-powered insights.")

# --- 1. Data Connection ---
def load_data():
    conn = sqlite3.connect("data.db")
    df = pd.read_sql_query("SELECT * FROM data", conn)
    conn.close()
    return df

df = load_data()

# --- 2. Layout (Two Columns) ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Visual Analytics")
    
    # Show the bar chart
    fig1 = plot_sales_by_product(df)
    st.pyplot(fig1)
    
    # Show the pie chart
    fig2 = plot_sales_by_region(df)
    st.pyplot(fig2)

with col2:
    st.subheader("AI Insights")
    
    if st.button("Generate AI Insights"):
        with st.spinner("Thinking..."):
            # Get the data summary using your existing analyzer function
            summary = get_summary(df)
            
            # Get the AI response
            insights = get_insights(summary)
            
            st.success("Analysis Complete!")
            st.markdown(insights)
    else:
        st.info("Click the button above to run the AI analyzer.")

# --- 3. Data Preview (Bottom) ---
with st.expander("View Raw Data"):
    st.dataframe(df)