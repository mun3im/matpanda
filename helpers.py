import pandas as pd

def calculate_total_revenue(df):
    """
    Adds a 'total_revenue' column to the DataFrame.
    total_revenue = units_sold * price_per_unit
    """
    df['total_revenue'] = df['units_sold'] * df['price_per_unit']
    return df

def get_top_products(df, n=3):
    """Returns top N products by total revenue."""
    return df.groupby('product')['total_revenue'].sum().nlargest(n)

def add_revenue(df):
    """Adds 'revenue' column: units * price."""
    df['revenue'] = df['units'] * df['price']
    return df
