import pandas as pd
# Sample data for sales transactions and customer information
sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 103, 104, 101],
    'Amount': [250, 300, 400, 500, 600],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}

customer_data = {
    'CustomerID': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, 35, 40, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Convert data into DataFrame
sales_df = pd.DataFrame(sales_data)
customers_df = pd.DataFrame(customer_data)

# Show basic structure of sales_df
print("Sales DataFrame:")
print(sales_df.head())

# 1. Exploring the dataset (using shape and describe)
print("\nShape of sales data:", sales_df.shape)  # Get number of rows and columns
print("\nSales data statistics:")
#print(sales_df.describe())  # Summary statistics
print("Sales dataframe", sales_df)
print("customers_df", customers_df)