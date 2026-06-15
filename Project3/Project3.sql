* Total Orders
SELECT COUNT(*) AS TotalOrders
FROM orders;

* Average Order Value
SELECT AVG(TotalPrice) AS AverageOrderValue
FROM orders;

* Total Revenue
SELECT SUM(TotalPrice) AS TotalRevenue
FROM orders;

* High Value Orders
SELECT *
FROM orders
WHERE TotalPrice > 1000;

* Product Popularity
SELECT Product,
       COUNT(*) AS TotalOrders
FROM orders
GROUP BY Product
ORDER BY TotalOrders DESC;

* Payment Method Analysis
SELECT PaymentMethod,
       COUNT(*) AS Count
FROM orders
GROUP BY PaymentMethod
ORDER BY Count DESC;

* Order Status Analysis
SELECT OrderStatus,
       COUNT(*) AS Count
FROM orders
GROUP BY OrderStatus
ORDER BY Count DESC;

* Referral Source Analysis
SELECT ReferralSource,
       COUNT(*) AS Count
FROM orders
GROUP BY ReferralSource
ORDER BY Count DESC;