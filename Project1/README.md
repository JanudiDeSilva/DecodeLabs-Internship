## Project 1: Data Cleaning & Preparation

### Overview

This project focuses on preparing a raw e-commerce dataset for analysis by cleaning, validating, and standardizing the data. The dataset contains **1,200 order records** across **14 columns**, providing a reliable foundation for subsequent analytics and visualization projects.

### Key Tasks

* Loaded and inspected the raw dataset.
* Handled missing values by replacing empty **CouponCode** entries with **"No Coupon"**.
* Removed duplicate records and verified that every **OrderID** is unique.
* Converted the **Date** column to datetime format.
* Converted numeric columns to appropriate data types.
* Standardized text fields by trimming whitespace and ensuring consistent formatting.
* Removed invalid records with non-positive quantities or prices.
* Recalculated **TotalPrice** (`Quantity × UnitPrice`) to ensure data consistency.
* Performed validation checks to confirm data integrity before saving.

### Result

The cleaned dataset retained all **1,200 records** and was saved as **Cleaned_Dataset.xlsx**, serving as the foundation for all subsequent projects.

### Key Takeaway

Data cleaning is a critical step in the analytics workflow. By handling missing values appropriately, validating records, and ensuring consistency across the dataset, the data becomes accurate, reliable, and ready for meaningful analysis.
