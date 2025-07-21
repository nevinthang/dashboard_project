import pandas as pd

# Baca raw data dengan encoding windows
df = pd.read_csv("Superstore.csv", encoding="windows-1252")

# Rename kolom agar lebih clean
df = df.rename(columns={
    'Row ID': 'RowID',
    'Order ID': 'OrderID',
    'Order Date': 'OrderDate',
    'Ship Date': 'ShipDate',
    'Ship Mode': 'ShipMode',
    'Customer ID': 'CustomerID',
    'Customer Name': 'CustomerName',
    'Postal Code': 'PostalCode',
    'Product ID': 'ProductID',
    'Sub-Category': 'SubCategoryID',
    'Product Name': 'ProductName'
})

# Customer.csv
customer = df[['CustomerID', 'CustomerName', 'Segment']].drop_duplicates()
customer.to_csv("Customer.csv", index=False)

# Location.csv
location = df[['PostalCode', 'Country', 'City', 'State', 'Region']].drop_duplicates()
location.to_csv("Location.csv", index=False)

# SubCategory.csv
subcategory = df[['SubCategoryID', 'Category']].drop_duplicates()
subcategory.to_csv("SubCategory.csv", index=False)

# Product.csv
product = df[['ProductID', 'SubCategoryID', 'ProductName']].drop_duplicates()
product.to_csv("Product.csv", index=False)

# Orders.csv
orders = df[['OrderID', 'OrderDate', 'ShipDate', 'ShipMode']].drop_duplicates()
orders.to_csv("Orders.csv", index=False)

# Master.csv (Fact Table)
master = df[['RowID', 'OrderID', 'CustomerID', 'PostalCode', 'ProductID', 'Sales', 'Quantity', 'Discount', 'Profit']]
master.to_csv("Master.csv", index=False)
