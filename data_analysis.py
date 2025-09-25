# 📌 Task 5: Data Analysis on CSV Files
# Tools: Python, Pandas, Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV file
df = pd.read_csv("C:/Users/Sona/Downloads/sales.csv")

# 2. Show first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# 3. Basic info
print("\nDataset Info:")
print(df.info())

# 4. Shape of DataFrame
print("\nShape of dataset (rows, columns):", df.shape)

# 5. Check for missing values
print("\nMissing values in dataset:")
print(df.isnull().sum())

# 6. Total revenue by product
revenue_by_product = df.groupby("Product")["Revenue"].sum()
print("\nRevenue by Product:")
print(revenue_by_product)

# 7. Total quantity sold by category
quantity_by_category = df.groupby("Category")["Quantity"].sum()
print("\nQuantity by Category:")
print(quantity_by_category)

# 8. Visualization - Revenue by Product
plt.figure(figsize=(8,5))
revenue_by_product.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()

# 9. Visualization - Quantity by Category
plt.figure(figsize=(6,4))
quantity_by_category.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Quantity Sold by Category")
plt.xlabel("Category")
plt.ylabel("Total Quantity")
plt.xticks(rotation=45)
plt.show()
