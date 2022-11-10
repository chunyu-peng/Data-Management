SELECT manufacturer as Manufacturer, AVG(price) as Average FROM Beers2Bars GROUP BY manufacturer;
/*
+----------------+---------+
| Manufacturer   | Average |
+----------------+---------+
| Anheuser-Busch |       3 |
| Heineken       |       2 |
| Pete's         |     3.5 |
+----------------+---------+
*/