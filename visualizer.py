import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean style for all plots
sns.set_theme(style="whitegrid")

def plot_sales_by_product(df):
    """Creates a bar chart showing total sales per product."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='product', y='sales', palette='viridis', ax=ax)
    ax.set_title("Total Sales by Product", fontsize=14)
    ax.set_xlabel("Product", fontsize=12)
    ax.set_ylabel("Sales ($)", fontsize=12)
    plt.tight_layout()
    return fig

def plot_quantity_distribution(df):
    """Creates a histogram to show how quantities are distributed."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['quantity'], kde=True, color='skyblue', ax=ax)
    ax.set_title("Distribution of Order Quantities", fontsize=14)
    ax.set_xlabel("Quantity", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    return fig

def plot_sales_by_region(df):
    """Creates a pie chart for regional sales contribution."""
    region_sales = df.groupby('region')['sales'].sum()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', 
           startangle=140, colors=sns.color_palette('pastel'))
    ax.set_title("Sales Contribution by Region", fontsize=14)
    plt.tight_layout()
    return fig

def plot_sales_over_time(df):
    """Creates a line chart showing sales trends over dates."""
    # Ensure date is in datetime format for plotting
    df['date'] = pd.to_datetime(df['date'])
    temp_df = df.sort_values('date')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=temp_df, x='date', y='sales', marker='o', ax=ax)
    ax.set_title("Sales Trend Over Time", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig




if __name__ == "__main__":
    import pandas as pd
    import matplotlib.pyplot as plt # Make sure this is imported
    
    test_data = pd.DataFrame({
        'product': ['Laptop', 'Phone'],
        'sales': [1000, 500],
        'quantity': [1, 2],
        'region': ['North', 'South'],
        'date': ['2026-03-01', '2026-03-02']
    })
    
    print("Generating test plot...")
    fig = plot_sales_by_product(test_data)
    
    # THIS LINE IS THE KEY:
    plt.show() 
    
    print("Success! Plot window opened.")