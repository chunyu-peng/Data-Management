CREATE VIEW Beers2Bars AS SELECT manf AS manufacturer, beer, bar, price FROM Beers INNER JOIN Sells ON Beers.name=Sells.beer;
/*
+----------------+------------+------------+-------+
| manufacturer   | beer       | bar        | price |
+----------------+------------+------------+-------+
| Anheuser-Busch | Bud        | Bob's bar  |     3 |
| Anheuser-Busch | Bud        | Joe's bar  |     3 |
| Anheuser-Busch | Bud        | Mary's bar |  NULL |
| Anheuser-Busch | Bud Lite   | Joe's bar  |     3 |
| Anheuser-Busch | Bud Lite   | Mary's bar |     3 |
| Heineken       | Budweiser  | Mary's bar |     2 |
| Anheuser-Busch | Michelob   | Joe's bar  |     3 |
| Pete's         | Summerbrew | Bob's bar  |     3 |
| Pete's         | Summerbrew | Joe's bar  |     4 |
+----------------+------------+------------+-------+
*/