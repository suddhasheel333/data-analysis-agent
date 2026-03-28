import pandas as pd
import sqlite3
import os

def load_csv(filepath):
    """Load a CSV file into a Pandas DataFrame"""
    df = pd.read_csv(filepath)
    print(f"Loaded CSV: {filepath}")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Columns: {list(df.columns)}")
    print(f"First 5 rows:")
    print(df.head())
    return df

def load_to_sqlite(df, db_name="data.db", table_name="data"):
    """Convert DataFrame to SQLite database"""
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Data loaded into SQLite → '{db_name}' (table: '{table_name}')")
    conn.close()

def run_query(query, db_name="data.db"):
    """Run any SQL query and return results"""
    conn = sqlite3.connect(db_name)
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

if __name__ == "__main__":
    # ── 1. Generate sample sales CSV ──────────────────────────────
    sample_data = {
        "date":     ["2024-01-01","2024-01-02","2024-01-03",
                     "2024-01-04","2024-01-05","2024-01-06"],
        "product":  ["Laptop","Phone","Tablet","Laptop","Phone","Tablet"],
        "category": ["Electronics","Electronics","Electronics",
                     "Electronics","Electronics","Electronics"],
        "sales":    [1200, 800, 450, 1500, 950, 600],
        "quantity": [2, 5, 3, 3, 7, 4],
        "region":   ["North","South","East","West","North","South"]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv("sample_data.csv", index=False)
    print("sample_data.csv created!")

    # ── 2. Load CSV ────────────────────────────────────────────────
    df = load_csv("sample_data.csv")

    # ── 3. Push to SQLite ──────────────────────────────────────────
    load_to_sqlite(df)

    # ── 4. Run SQL queries ─────────────────────────────────────────
    print("Total sales by product:")
    print(run_query("SELECT product, SUM(sales) as total_sales FROM data GROUP BY product ORDER BY total_sales DESC"))

    print("Average sales by region:")
    print(run_query("SELECT region, AVG(sales) as avg_sales FROM data GROUP BY region"))

    print("Top selling product by quantity:")
    print(run_query("SELECT product, SUM(quantity) as total_qty FROM data GROUP BY product ORDER BY total_qty DESC LIMIT 1"))