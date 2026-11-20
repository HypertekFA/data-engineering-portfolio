SELECT * FROM customers;

SELECT customer_name, contact_name, address
FROM customers
Where country = 'Germany';

SELECT * FROM customers
WHERE country = 'Germany' AND city = 'Berlin';

SELECT customer_name, contact_name, address
FROM customers
WHERE country in ('Germany', 'France', 'UK');

SELECT customer_name, count(*) AS total_customers
FROM customers
WHERE country in ('Germany', 'France', 'UK')
group by customer_name
having count(*) > 1;


