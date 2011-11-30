BEGIN TRANSACTION;
CREATE TABLE planetData (planetID INTEGER PRIMARY KEY, planetName TEXT, planetDis REAL, planetScale REAL, planetPosX REAL, planetPosY REAL, planetPosZ REAL);
INSERT INTO planetData VALUES(1,'Sun',NULL,0.008,0.483,0.154,0.0);
INSERT INTO planetData VALUES(2,'Mercury',NULL,0.0012,0.15,0.15,0.0);
INSERT INTO planetData VALUES(3,'Venus',NULL,NULL,NULL,NULL,NULL);
INSERT INTO planetData VALUES(4,'Earth',NULL,NULL,NULL,NULL,NULL);
INSERT INTO planetData VALUES(5,'Mars',NULL,NULL,NULL,NULL,NULL);
INSERT INTO planetData VALUES(6,'Jupiter',NULL,NULL,NULL,NULL,NULL);
INSERT INTO planetData VALUES(7,'Saturn',NULL,NULL,NULL,NULL,NULL);
INSERT INTO planetData VALUES(8,'Uranus',NULL,NULL,NULL,NULL,NULL);
INSERT INTO planetData VALUES(9,'Neptune',NULL,NULL,NULL,NULL,NULL);
INSERT INTO planetData VALUES(10,'Pluto',NULL,NULL,NULL,NULL,NULL);
CREATE TABLE stationData (stationName TEXT, stationPosX REAL, stationPosY REAL, stationPosZ REAL, stationScale REAL);
COMMIT;