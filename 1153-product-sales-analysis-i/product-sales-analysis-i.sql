# Write your MySQL query statement below
select product.product_name, Sales.year, Sales.price 
from Sales 
join Product using(product_id)