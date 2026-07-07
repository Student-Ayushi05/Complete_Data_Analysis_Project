import pandas as pd
import matplotlib.pyplot as plt


# LOAD DATASET

df = pd.read_csv("data/sales_data.csv")

print("="*50)
print("First 5 Rows")
print("="*50)
print(df.head())

print("\nDataset Information")
print(df.info())


#Checking missing values

print("\nMissing Values")
print(df.isnull().sum())


# DATA CLEANING

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create Month column
df['Month'] = df['Date'].dt.strftime('%b')

print("\nSummary Statistics")
print(df.describe())


# KPI ANALYSIS

total_sales = df['Total_Sales'].sum()
total_orders = len(df)
total_quantity = df['Quantity'].sum()
average_sales = df['Total_Sales'].mean()

#Best Selling Product
best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)

print("\n========== KPIs ==========")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Order Value: ₹{average_sales:,.2f}")
print(f"Best Selling Product: {best_product}")


# PRODUCT ANALYSIS

product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)

print("\nSales by Product")
print(product_sales)


# REGION ANALYSIS

region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)

print("\nSales by Region")
print(region_sales)


# MONTHLY SALES

monthly_sales = df.groupby('Month')['Total_Sales'].sum()

month_order = ['Jan','Feb','Mar','Apr','May','Jun',
               'Jul','Aug','Sep','Oct','Nov','Dec']

monthly_sales = monthly_sales.reindex(month_order)

print("\nMonthly Sales")
print(monthly_sales)


# CHART 1
# Product Sales

plt.figure(figsize=(8,5))
product_sales.plot(kind='bar')

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()


# CHART 2
# Monthly Sales Trend

plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.grid(True)

plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()


# CHART 3
# Region Sales

plt.figure(figsize=(6,6))
region_sales.plot(kind='pie', autopct='%1.1f%%')

plt.title("Regional Sales Distribution")
plt.ylabel("")

plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()


# CHART 4
# Quantity Distribution

plt.figure(figsize=(8,5))
plt.hist(df['Quantity'], bins=10)

plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("quantity_distribution.png")
plt.show()


# CHART 5
# Price vs Total Sales

plt.figure(figsize=(8,5))
plt.scatter(df['Price'], df['Total_Sales'])

plt.title("Price vs Total Sales")
plt.xlabel("Price")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("price_vs_sales.png")
plt.show()


# BUSINESS INSIGHTS

print("\n-------- BUSINESS INSIGHTS -------- \n")

print(f"1. Total Revenue Generated: ₹{total_sales:,.2f}")

print(f"2. Highest Selling Product: {product_sales.idxmax()}")

print(f"3. Highest Revenue Region: {region_sales.idxmax()}")

print(f"4. Total Quantity Sold: {total_quantity}")

print(f"5. Average Order Value: ₹{average_sales:,.2f}")

print("\nAnalysis Completed Successfully!")