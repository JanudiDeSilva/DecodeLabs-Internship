import pandas as pd
import numpy as np

df = pd.read_excel(r"E:\DecodeLabs-Internship\Dataset for Data Analytics.xlsx")
print(df.head())
print("Initial shape:", df.shape)

#Missing values check 
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Duplicate rows check 
print("\nDuplicate rows before cleaning:", df.duplicated().sum())

#  Fill missing CouponCode values
print("\nMissing CouponCode values:", df["CouponCode"].isnull().sum())
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

#  Remove duplicate rows 
df = df.drop_duplicates()

# Enforce unique OrderID 
before = len(df)
df = df.drop_duplicates(subset="OrderID", keep="first")
print(f"\nRemoved {before - len(df)} duplicate OrderID rows")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

#  Coerce numeric columns to proper numeric types 
numeric_cols = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

#  Trim whitespace and standardize case in text columns 
text_cols = ["Product", "PaymentMethod", "OrderStatus", "ReferralSource",
             "ShippingAddress", "CustomerID", "OrderID", "TrackingNumber", "CouponCode"]
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# Standardize categorical-like text to Title Case 
for col in ["Product", "PaymentMethod", "OrderStatus", "ReferralSource"]:
    df[col] = df[col].str.title()

#Recompute nulls introduced by numeric coercion, then handle them 
print("\nMissing values after type coercion:")
print(df.isnull().sum())

for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

# FIX: Sanity check for invalid values 
invalid_qty = df[df["Quantity"] <= 0]
invalid_price = df[df["UnitPrice"] <= 0]
print(f"\nInvalid Quantity rows (<=0): {len(invalid_qty)}")
print(f"Invalid UnitPrice rows (<=0): {len(invalid_price)}")
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Recalculate TotalPrice to guarantee consistency 
df["TotalPrice"] = (df["Quantity"] * df["UnitPrice"]).round(2)

#Final verification 
print("\nDuplicate OrderIDs after cleaning:", df["OrderID"].duplicated().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())
print("Missing values after cleaning:")
print(df.isnull().sum())
print("Final shape:", df.shape)

assert df["OrderID"].duplicated().sum() == 0, "Duplicate OrderIDs still exist!"
assert df["Date"].isnull().sum() == 0, "Some dates failed to parse!"
print("\nVerified: zero duplicate IDs, zero invalid dates.")


df.to_excel("Cleaned_Dataset.xlsx", index=False)
print("\nCleaned dataset saved successfully.")