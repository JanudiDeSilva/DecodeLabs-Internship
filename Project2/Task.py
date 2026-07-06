import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

df = pd.read_excel(r"E:\DecodeLabs-Internship\Project1\Cleaned_Dataset.xlsx")
print("Dataset Shape:", df.shape)

print("\nDataset Information:")
df.info()

print("\nDataset Description:")
print(df.describe())

print("\nMean Values")
print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].mean())

print("\nMedian Values")
print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].median())

print("\nTop Products")
print(df["Product"].value_counts())

print("\nPayment Methods")
print(df["PaymentMethod"].value_counts())

print("\nOrder Status")
print(df["OrderStatus"].value_counts())

print("\nReferral Sources")
print(df["ReferralSource"].value_counts())

# Outlier detection 
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["TotalPrice"] < lower) | (df["TotalPrice"] > upper)]
print("\nNumber of Outliers:", len(outliers))
print("Outlier bounds -> lower:", round(lower, 2), "upper:", round(upper, 2))

# Correlation analysis 
numeric_cols = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]]
corr = numeric_cols.corr()
print("\nCorrelation Matrix:")
print(corr)

plt.figure(figsize=(7, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Numeric Variables")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Distribution visualization (kit conclusion suggests this too) 
plt.figure(figsize=(8, 5))
sns.histplot(df["TotalPrice"], bins=30, kde=True, color="coral")
plt.title("TotalPrice Distribution")
plt.tight_layout()
plt.savefig("totalprice_distribution.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df["TotalPrice"], color="skyblue")
plt.title("TotalPrice Outlier Check (Boxplot)")
plt.tight_layout()
plt.savefig("totalprice_boxplot.png")
plt.close()

print("\nEDA complete. Charts saved: correlation_heatmap.png, totalprice_distribution.png, totalprice_boxplot.png")