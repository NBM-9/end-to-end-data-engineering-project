-- Total revenue by region
SELECT region, SUM(total_amount) AS revenue
FROM sales
GROUP BY region;

-- Top selling product
SELECT product, SUM(quantity) AS total_sold
FROM sales
GROUP BY product
ORDER BY total_sold DESC
LIMIT 1;

-- Monthly revenue
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(total_amount) AS revenue
FROM sales
GROUP BY month;
