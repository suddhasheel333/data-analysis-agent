import os
import pandas as pd
import sqlite3
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_summary(df):
    summary = {}
    summary["rows"] = df.shape[0]
    summary["columns"] = df.shape[1]
    summary["numeric_columns"] = list(df.select_dtypes(include="number").columns)
    summary["text_columns"] = list(df.select_dtypes(include="object").columns)
    missing = df.isnull().sum()
    summary["missing_values"] = missing[missing > 0].to_dict()
    summary["stats"] = df.describe().to_string()
    summary["value_counts"] = {}
    for col in summary["text_columns"]:
        summary["value_counts"][col] = df[col].value_counts().to_dict()
    return summary

def print_summary(summary):
    print("\n--- DATA SUMMARY ---")
    print(f"Rows: {summary['rows']}")
    print(f"Columns: {summary['columns']}")
    print(f"\nNumeric columns: {summary['numeric_columns']}")
    print(f"Text columns: {summary['text_columns']}")
    print(f"\nMissing values: {summary['missing_values'] if summary['missing_values'] else 'None'}")
    print(f"\nStatistics:\n{summary['stats']}")
    print(f"\nValue counts:")
    for col, counts in summary["value_counts"].items():
        print(f"  {col}: {counts}")

def get_insights(summary):
    prompt = f"""
    You are a data analyst. Analyze the following dataset summary and provide exactly 5 key insights.
    Be specific, concise, and focus on patterns, anomalies, and business implications.

    Dataset Summary:
    - Rows: {summary['rows']}
    - Columns: {summary['columns']}
    - Numeric columns: {summary['numeric_columns']}
    - Text columns: {summary['text_columns']}
    - Missing values: {summary['missing_values']}
    - Statistics: {summary['stats']}
    - Value counts: {summary['value_counts']}

    Provide exactly 5 insights, numbered 1 to 5. Each insight should be 1-2 sentences.
    """
    print("\n--- SENDING DATA TO GROQ ---")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    try:
        conn = sqlite3.connect("data.db")
        df = pd.read_sql_query("SELECT * FROM data", conn)
        conn.close()
        print("Data loaded from SQLite database.")

        summary = get_summary(df)
        print_summary(summary)

        insights = get_insights(summary)
        print("\n--- AI INSIGHTS ---")
        print(insights)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")