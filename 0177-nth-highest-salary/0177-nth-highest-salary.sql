CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    SELECT
      MAX(salary) INTO result
      FROM (
        SELECT
            salary,
            DENSE_RANK() OVER (order by salary desc) rk
         FROM Employee
      ) re
    WHERE re.rk = N;
    RETURN result;
END;