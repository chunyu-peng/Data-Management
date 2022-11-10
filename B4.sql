SELECT bar as Bar FROM Sells WHERE price=(SELECT MAX(price) FROM Sells);
/*
+-----------+
| Bar       |
+-----------+
| Joe's bar |
+-----------+
*/