import pandas as pd
import sqlite3

df = pd.read_excel(r"E:\DecodeLabs-Internship\Project1\Cleaned_Dataset.xlsx")

conn = sqlite3.connect("DecodeLabs.db")

df.to_sql("orders", conn, if_exists="replace", index=False)

result = pd.read_sql("SELECT COUNT(*) AS TotalOrders FROM orders;", conn)
print(result)

conn.close()