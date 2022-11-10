SELECT dept_no FROM (SELECT dept_no, COUNT(emp_no) as managerNum FROM dept_manager GROUP BY dept_no) as managerTable WHERE managerNum>=3;
/*
+---------+
| dept_no |
+---------+
| d004    |
| d006    |
| d009    |
+---------+
*/