# Write your MySQL query statement below
select u.name as NAME, sum(t.amount) as BALANCE 
  from Transactions as t, Users as u
where t.account = u.account
group by name
having BALANCE > 10000