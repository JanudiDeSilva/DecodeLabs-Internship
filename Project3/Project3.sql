-- Total Orders
SELECT COUNT(*) AS TotalOrders
FROM orders;

-- Average Order Value
SELECT AVG(TotalPrice) AS AverageOrderValue
FROM orders;

-- Total Revenue
SELECT SUM(TotalPrice) AS TotalRevenue
FROM orders;

-- High Value Orders
SELECT *
FROM orders
WHERE TotalPrice > 1000
ORDER BY TotalPrice DESC;

-- Product Popularity
SELECT Product,
       COUNT(*) AS TotalOrders
FROM orders
GROUP BY Product
ORDER BY TotalOrders DESC;

-- Payment Method Analysis
SELECT PaymentMethod,
       COUNT(*) AS Count
FROM orders
GROUP BY PaymentMethod
ORDER BY Count DESC;

-- Order Status Analysis
SELECT OrderStatus,
       COUNT(*) AS Count
FROM orders
GROUP BY OrderStatus
ORDER BY Count DESC;

-- Referral Source Analysis
SELECT ReferralSource,
       COUNT(*) AS Count
FROM orders
GROUP BY ReferralSource
ORDER BY Count DESC;

-- Products appearing more than 150 times (HAVING clause on aggregates)
SELECT Product,
       COUNT(*) AS TotalOrders
FROM orders
GROUP BY Product
HAVING COUNT(*) > 150
ORDER BY TotalOrders DESC;

--  Percentage contribution of each payment method to total orders
SELECT PaymentMethod,
       COUNT(*) AS Count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 2) AS PercentageOfTotal
FROM orders
GROUP BY PaymentMethod
ORDER BY PercentageOfTotal DESC;

--  Percentage contribution of each order status
SELECT OrderStatus,
       COUNT(*) AS Count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 2) AS PercentageOfTotal
FROM orders
GROUP BY OrderStatus
ORDER BY PercentageOfTotal DESC;



--- Average order value per referral source 
SELECT ReferralSource,
       COUNT(*) AS TotalOrders,
       ROUND(AVG(TotalPrice), 2) AS AvgOrderValue
FROM orders
GROUP BY ReferralSource
ORDER BY AvgOrderValue DESC;