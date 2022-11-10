SELECT first_name, last_name, title FROM employees INNER JOIN titles ON employees.emp_no=titles.emp_no WHERE title LIKE '%engineer%' and from_date>='2000-3-23';
/*
The output is too long, I can't copy this much.
*/