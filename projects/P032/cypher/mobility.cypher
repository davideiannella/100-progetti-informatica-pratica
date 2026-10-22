MERGE (a:Stop {id:'A'}) SET a.name='Centro'
MERGE (b:Stop {id:'B'}) SET b.name='Stazione'
MERGE (c:Stop {id:'C'}) SET c.name='Universita'
MERGE (a)-[ab:CONNECTS]->(b) SET ab.minutes=5
MERGE (b)-[bc:CONNECTS]->(c) SET bc.minutes=7
MERGE (a)-[ac:CONNECTS]->(c) SET ac.minutes=20;
MATCH p=(:Stop {id:'A'})-[:CONNECTS*1..4]->(:Stop {id:'C'})
RETURN p, reduce(total=0, r IN relationships(p) | total+r.minutes) AS minutes
ORDER BY minutes LIMIT 1;
