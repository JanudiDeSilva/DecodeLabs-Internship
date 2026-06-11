import pandas as pd
df = pd.read_excel("E:\\DecodeLabs-Internship\\Project1\\Cleaned_Dataset.xlsx")
print("Dataset Shape:", df.shape)


print("\nDataset Information:")
df.info()

print("\nDataset Description:")
print(df.describe())

print("\nMean Values")
print(df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].mean())

print("\nMedian Values")
print(df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].median())

print("\nTop 10 Products")
print(df["Product"].value_counts().head(10))

print("\nPayment Methods")
print(df["PaymentMethod"].value_counts())

print("\nOrder Status")
print(df["OrderStatus"].value_counts())

print("\nReferral Sources")
print(df["ReferralSource"].value_counts())

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["TotalPrice"] < lower) |
              (df["TotalPrice"] > upper)]

print("\nNumber of Outliers:", len(outliers))