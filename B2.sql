SELECT drinker as Drinker FROM (SELECT drinker, COUNT(bar) as count FROM Frequents GROUP BY drinker) as tb1 WHERE count=1;
/*
+----------+
| Drinker  |
+----------+
| Bill     |
| David    |
| Jennifer |
+----------+
*/