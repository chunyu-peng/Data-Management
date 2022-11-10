SELECT drinker as Drinker FROM Likes where beer='Bud' and drinker !=(SELECT tb1.drinker FROM (SELECT drinker From Likes where beer='Bud') as tb1 INNER JOIN (SELECT drinker From Likes where beer='Summerbrew') as tb2 ON tb1.drinker=tb2.drinker);
/*
+----------+
| Drinker  |
+----------+
| Bill     |
| Jennifer |
+----------+
*/