/* Write your PL/SQL query statement below */

SELECT
  CASE 
  WHEN count(*) >= 1 THEN MAX(salary)
  ELSE NULL
  END AS SecondHighestSalary
  FROM (
    SELECT
        salary,
        DENSE_RANK() OVER (order by salary desc) rk
     FROM Employee
  ) re
WHERE re.rk = 2  
  
 