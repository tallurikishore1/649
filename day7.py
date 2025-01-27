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

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(sales_df.head())

# Print basic statistics of the numerical columns
print("\nBasic statistics of the numerical columns:")
print(sales_df.describe())

# Calculate the total sales for each region
total_sales_by_region = sales_df.groupby('Region')['Sales'].sum()
print("\nTotal sales for each region:")
print(total_sales_by_region)

# Find the most sold product (based on quantity)
most_sold_product = sales_df.groupby('Product')['Quantity'].sum().idxmax()
print("\nMost sold product (based on quantity):")
print(most_sold_product)

# Compute the average profit margin for each product
sales_df['ProfitMargin'] = (sales_df['Profit'] / sales_df['Sales']) * 100
average_profit_margin_by_product = sales_df.groupby('Product')['ProfitMargin'].mean()
print("\nAverage profit margin for each product:")
print(average_profit_margin_by_product)