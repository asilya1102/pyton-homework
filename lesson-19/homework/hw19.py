Homework Assignment 1: Analyzing Sales Data

import pandas as pd

# Загружаем данные
sales = pd.read_csv("task/sales_data.csv")

# 1. Агрегаты по категориям
category_stats = sales.groupby("Category").agg(
    total_quantity=("Quantity", "sum"),
    avg_price=("Price", "mean"),
    max_quantity=("Quantity", "max")
)
print(category_stats)

# 2. Топ-продукт в каждой категории
top_products = sales.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_products = top_products.loc[top_products.groupby("Category")["Quantity"].idxmax()]
print(top_products)

# 3. Дата с максимальными продажами
sales["TotalSales"] = sales["Quantity"] * sales["Price"]
max_sales_date = sales.groupby("Date")["TotalSales"].sum().idxmax()
print("Date with highest sales:", max_sales_date)

Homework Assignment 2: Examining Customer Orders

import pandas as pd

orders = pd.read_csv("task/customer_orders.csv")

# 1. Фильтр по количеству заказов
customer_orders_count = orders.groupby("CustomerID")["OrderID"].count()
valid_customers = customer_orders_count[customer_orders_count >= 20].index
filtered_orders = orders[orders["CustomerID"].isin(valid_customers)]
print("Customers with >= 20 orders:", valid_customers)

# 2. Средняя цена > 120
avg_price_per_customer = orders.groupby("CustomerID")["Price"].mean()
high_spenders = avg_price_per_customer[avg_price_per_customer > 120].index
print("Customers with avg price > 120:", high_spenders)

# 3. Сумма и количество по продуктам
product_stats = orders.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", "sum")
)
filtered_products = product_stats[product_stats["total_quantity"] >= 5]
print(filtered_products)

Homework Assignment 3: Population Salary Analysis
import sqlite3
import pandas as pd

# 1. Чтение из базы
conn = sqlite3.connect("task/population.db")
population = pd.read_sql("SELECT * FROM population", conn)
conn.close()

# 2. Чтение Salary Bands
bands = pd.read_excel("task/population salary analysis.xlsx")

# Допустим, bands содержит колонки: Band, MinSalary, MaxSalary
def categorize_salary(salary):
    for _, row in bands.iterrows():
        if row["MinSalary"] <= salary <= row["MaxSalary"]:
            return row["Band"]
    return "Unknown"

population["SalaryBand"] = population["Salary"].apply(categorize_salary)

# 3. Метрики по категориям
band_stats = population.groupby("SalaryBand").agg(
    percentage=("SalaryBand", lambda x: len(x) / len(population) * 100),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median"),
    count=("Salary", "count")
)
print(band_stats)

# 4. Метрики по штатам
state_band_stats = population.groupby(["State", "SalaryBand"]).agg(
    percentage=("SalaryBand", lambda x: len(x) / len(population) * 100),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median"),
    count=("Salary", "count")
)
print(state_band_stats)
