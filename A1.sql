SELECT emp_no FROM employees WHERE first_name LIKE '%mary%' AND SUBSTR(last_name, -2, 1) = 'o';
/*
+--------+
| emp_no |
+--------+
|  16021 |
|  21756 |
|  52983 |
|  73998 |
|  78783 |
|  88698 |
| 101753 |
| 216534 |
| 263268 |
| 410311 |
| 423386 |
| 459548 |
| 491899 |
+--------+
*/