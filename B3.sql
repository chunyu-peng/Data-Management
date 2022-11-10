SELECT bar as Bar, COUNT(beer) as Total From Sells WHERE price>=2 GROUP BY bar;
/*
+------------+-------+
| Bar        | Total |
+------------+-------+
| Bob's bar  |     2 |
| Joe's bar  |     4 |
| Mary's bar |     2 |
+------------+-------+
*/