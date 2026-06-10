Working with codex on this
Practice Task

select drivers.city, count(drivers.name) as Total_Members, sum(trips.fare_amount)
from drivers
join trips
on drivers.driver_id = trips.trip_id
group by drivers.city

All products, including products with zero sales, with total quantity sold and total revenue by product name.

select products.product_name, coalesce(sum(sales.quantity), 0)
as total_quantity, coalesce(sum(sales.revenue), 0) as total_revenue
from products
left join sales
on products.product_id = sales.product_id
group by product.product_name
