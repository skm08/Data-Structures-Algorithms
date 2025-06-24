# Write your MySQL query statement below
select distinct customer_id, count(*) as count_no_trans 
from visits
left join Transactions using(visit_id)
where transaction_id is null
group by customer_id;