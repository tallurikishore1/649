import pandas as pd

# Sample data for sales transactions
sales_data = {
    'Date': ['2023-01-02', '2023-01-03', '2023-01-03', '2023-01-20', '2023-01-04', '2023-01-17',
             '2023-01-14', '2023-01-07', '2023-01-11', '2023-01-01', '2023-01-19', '2023-01-12',
             '2023-01-09', '2023-01-10', '2023-01-08', '2023-01-05', '2023-01-15', '2023-01-18',
             '2023-01-13', '2023-01-16'],
    'Product': ['Tablet', 'Laptop', 'Tablet', 'Tablet', 'Laptop', 'Tablet', 'Keyboard', 'Smartphone',
                'Smartphone', 'Laptop', 'Monitor', 'Laptop', 'Monitor', 'Smartphone', 'Laptop',
                'Keyboard', 'Tablet', 'Monitor', 'Tablet', 'Tablet'],
    'Region': ['East', 'North', 'East', 'North', 'West', 'North', 'East', 'East', 'West', 'North',
               'North', 'West', 'North', 'North', 'East', 'North', 'North', 'West', 'West', 'South'],
    'Sales': [1061.81, 1926.07, 1597.99, 1397.99, 734.03, 733.99, 587.13, 1799.26, 1401.67, 1562.11,
              530.88, 1954.86, 1748.66, 818.51, 772.74, 775.11, 956.36, 1287.13, 1147.92, 936.84],
    'Profit': [236.12, 246.34, 253.17, 242.23, 140.36, 188.66, 82.16, 364.97, 306.24, 170.72,
               117.59, 262.16, 197.62, 237.19, 226.51, 202.83, 153.9, 153.86, 271.88, 176.15],
    'Quantity': [7, 8, 3, 4, 4, 4, 9, 4, 4, 6, 5, 6, 6, 2, 3, 4, 8, 6, 9, 8]
}

# Convert data into DataFrame
sales_df = pd.DataFrame(sales_data)

# Data Filtering
# Extract all rows where sales are greater than 1000
high_sales_df = sales_df[sales_df['Sales'] > 1000]
print("Rows where sales are greater than 1000:")
print(high_sales_df)

# Find all sales records for a specific region (e.g., "East")
east_sales_df = sales_df[sales_df['Region'] == 'East']
print("\nSales records for the 'East' region:")
print(east_sales_df)

# Data Processing
# Add a new column, Profit_Per_Unit, calculated as Profit / Quantity
sales_df['Profit_Per_Unit'] = sales_df['Profit'] / sales_df['Quantity']
print("\nData with Profit_Per_Unit column added:")
print(sales_df)

# Create another column, High_Sales, which labels rows as Yes if Sales > 1000, else No
sales_df['High_Sales'] = sales_df['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')
print("\nData with High_Sales column added:")
print(sales_df)
