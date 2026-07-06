import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")

# Load dataset
df = pd.read_excel(r"E:\DecodeLabs-Internship\Project1\Cleaned_Dataset.xlsx")

# Create output folder
output_dir = "Project4_Charts"
os.makedirs(output_dir, exist_ok=True)

# 1. Top Products by Order Count
plt.figure(figsize=(10, 6))
top_products = df["Product"].value_counts()

sns.barplot(
    x=top_products.values,
    y=top_products.index,
    hue=top_products.index,
    palette="viridis",
    legend=False
)

plt.title("Products by Order Count")
plt.xlabel("Number of Orders")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(f"{output_dir}/products_by_order_count.png")
plt.close()

# 2. Payment Method Distribution
plt.figure(figsize=(7, 7))
payment_counts = df["PaymentMethod"].value_counts()

plt.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Method Distribution")
plt.tight_layout()
plt.savefig(f"{output_dir}/payment_method_distribution.png")
plt.close()

# 3. Order Status Breakdown
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="OrderStatus",
    hue="OrderStatus",
    order=df["OrderStatus"].value_counts().index,
    palette="Set2",
    legend=False
)

plt.title("Order Status Breakdown")
plt.xlabel("Order Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(f"{output_dir}/order_status_breakdown.png")
plt.close()

# 4. Referral Source Distribution
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    y="ReferralSource",
    hue="ReferralSource",
    order=df["ReferralSource"].value_counts().index,
    palette="mako",
    legend=False
)

plt.title("Orders by Referral Source")
plt.xlabel("Count")
plt.ylabel("Referral Source")
plt.tight_layout()
plt.savefig(f"{output_dir}/referral_source_distribution.png")
plt.close()

# 5. TotalPrice Distribution + Outlier Check
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["TotalPrice"], color="skyblue")
plt.title("TotalPrice Distribution (Outlier Check)")
plt.tight_layout()
plt.savefig(f"{output_dir}/totalprice_boxplot.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.histplot(
    df["TotalPrice"],
    bins=30,
    kde=True,
    color="coral"
)
plt.title("TotalPrice Distribution")
plt.xlabel("Total Price")
plt.tight_layout()
plt.savefig(f"{output_dir}/totalprice_histogram.png")
plt.close()

# 6. Correlation Heatmap
plt.figure(figsize=(7, 6))

numeric_cols = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]]
corr = numeric_cols.corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Numeric Variables")
plt.tight_layout()
plt.savefig(f"{output_dir}/correlation_heatmap.png")
plt.close()

# 7. Monthly Order Trend

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_orders = df.groupby("Month")["OrderID"].count()

plt.figure(figsize=(10, 5))

monthly_orders.plot(
    kind="line",
    marker="o",
    color="darkgreen"
)

plt.title("Monthly Order Trend")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_dir}/monthly_order_trend.png")
plt.close()

# 8. Revenue by Product
revenue_by_product = (
    df.groupby("Product")["TotalPrice"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=revenue_by_product.values,
    y=revenue_by_product.index,
    hue=revenue_by_product.index,
    palette="crest",
    legend=False
)

plt.title("Total Revenue by Product")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(f"{output_dir}/revenue_by_product.png")
plt.close()

print(f"All charts saved successfully in the '{output_dir}' folder.")