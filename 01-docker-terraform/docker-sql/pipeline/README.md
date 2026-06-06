Working with codex on this
Practice Task

SELECT
  customers.city,
  SUM(orders.amount) AS total_revenue
FROM customers
JOIN orders
ON orders.order_id
GROUP BY orders.city;