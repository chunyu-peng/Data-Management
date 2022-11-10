SELECT manf AS Manufacturer FROM (SELECT manf, COUNT(name) AS count FROM Beers GROUP BY manf) AS tb1 WHERE count >= 3;
/*
+----------------+
| Manufacturer   |
+----------------+
| Anheuser-Busch |
+----------------+
*/