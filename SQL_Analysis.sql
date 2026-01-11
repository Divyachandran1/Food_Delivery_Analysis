CREATE DATABASE food_delivery_db;

SHOW DATABASES;
USE food_delivery_db;

SELECT COUNT(*) FROM food_delivery_orders;

SELECT * FROM food_delivery_orders LIMIT 5;
-- Identify top spending customers
SELECT 
    Customer_ID,
    SUM(Final_Amount) AS Total_Spent,
    COUNT(Order_ID) AS Total_Orders
FROM food_delivery_orders
GROUP BY Customer_ID
ORDER BY Total_Spent DESC
LIMIT 10;
-- Weekend vs weekday order patterns
SELECT 
    Order_Day_Type,
    COUNT(*) AS Total_Orders,
    AVG(Order_Value) AS Avg_Order_Value
FROM food_delivery_orders
GROUP BY Order_Day_Type;
-- Revenue & Profit Analysis Monthly revenue trends
SELECT 
    DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
    SUM(Final_Amount) AS Monthly_Revenue
FROM food_delivery_orders
GROUP BY Month
ORDER BY Month;

-- Impact of discounts on profit
SELECT 
    Discount_Applied,
    AVG(Profit_Margin) AS Avg_Profit
FROM food_delivery_orders
GROUP BY Discount_Applied
ORDER BY Discount_Applied;
-- Delivery Performance Average delivery time by city
SELECT 
    City,
    SUM(Final_Amount) AS Revenue
FROM food_delivery_orders
GROUP BY City
ORDER BY Revenue DESC
LIMIT 5;

SELECT 
    Cuisine_Type,
    SUM(Final_Amount) AS Revenue
FROM food_delivery_orders
GROUP BY Cuisine_Type
ORDER BY Revenue DESC
LIMIT 5;
-- Distance vs delivery delay analysis
SELECT 
    City,
    AVG(Delivery_Time_Min) AS Avg_Delivery_Time
FROM food_delivery_orders
GROUP BY City
ORDER BY Avg_Delivery_Time;
-- Delivery rating vs delivery time
SELECT 
    Delivery_Rating,
    AVG(Delivery_Time_Min) AS Avg_Time
FROM food_delivery_orders
GROUP BY Delivery_Rating
ORDER BY Delivery_Rating DESC;
-- Restaurant Performance
-- Top-rated restaurants
SELECT 
    Restaurant_Name,
    AVG(Restaurant_Rating) AS Avg_Rating
FROM food_delivery_orders
GROUP BY Restaurant_Name
HAVING COUNT(*) > 50
ORDER BY Avg_Rating DESC
LIMIT 10;
-- Cancellation rate by restaurant
SELECT 
    Restaurant_Name,
    COUNT(CASE WHEN Order_Status='Cancelled' THEN 1 END) * 100.0 / COUNT(*) AS Cancellation_Rate
FROM food_delivery_orders
GROUP BY Restaurant_Name
ORDER BY Cancellation_Rate DESC;
-- Operational Insights 
-- Peak hour demand analysis
SELECT 
    Peak_Hour,
    COUNT(*) AS Total_Orders
FROM food_delivery_orders
GROUP BY Peak_Hour;
-- Payment Mode Preferences 
SELECT 
    Payment_Mode,
    COUNT(*) AS Usage_Count
FROM food_delivery_orders
GROUP BY Payment_Mode
ORDER BY Usage_Count DESC;
-- Cancellation Reason Analysis
SELECT 
    Cancellation_Reason,
    COUNT(*) AS Count
FROM food_delivery_orders
WHERE Order_Status='Cancelled'
GROUP BY Cancellation_Reason
ORDER BY Count DESC;

