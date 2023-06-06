# Write your MySQL query statement below
select ee.name as Employee
  from Employee ee
 left join Employee em
   on ee.managerId = em.id
 where ee.salary > em.salary