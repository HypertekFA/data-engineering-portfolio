SELECT COUNT(country),
customer_id, customer_name, country
FROM customers
GROUP BY customer_id, customer_name, country
ORDER BY country DESC;

SELECT * FROM orders;
SELECT * FROM products;

SELECT unit, product_name, SUM(price)
FROM products
WHERE price > 13
GROUP BY unit, product_name
ORDER BY unit;

SELECT unit, product_name, Max(price)
FROM products
WHERE price > 13
GROUP BY unit, product_name
ORDER BY unit;

SELECT unit, product_name, AVG(price)
FROM products
WHERE price > 13
GROUP BY unit, product_name
ORDER BY unit;

SELECT unit, product_name, MIN(price)
FROM products
WHERE price > 13
GROUP BY unit, product_name
ORDER BY unit