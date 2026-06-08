import pandas as pd
import numpy as np


df = pd.read_excel(r"E:\DecodeLabs-Internship\Dataset for Data Analytics.xlsx")
print(df.head())

print("Initial shape:", df.shape)

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate rows before cleaning:", df.duplicated().sum())

# Fill missing CouponCode values
print("\nMissing CouponCode values:", df["CouponCode"].isnull().sum())

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print("Missing CouponCode values after cleaning:",
      df["CouponCode"].isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Check duplicate Order IDs
print("\nDuplicate Order IDs:", df["OrderID"].duplicated().sum())

# Final check
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:", df.duplicated().sum())

print("\nFinal shape:", df.shape)

# Save cleaned dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nCleaned dataset saved successfully.")