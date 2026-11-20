SELECT COUNT(country),
customer_id, customer_name, country
FROM customers
GROUP BY customer_id, customer_name, country
ORDER BY country DESC