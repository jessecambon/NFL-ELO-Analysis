# NFL ELO Analysis

Author: Jesse Cambon, myfullname -a/t- gmail


Date: 10/2/2017

Description:

Scrapes NFL results from pro-football-reference and calculates ELO ratings for each team
for the 2017-2018 season

Initializes the ELO ratings for the year using https://projects.fivethirtyeight.com/2017-nfl-predictions/

My ELO lines up fairly closely with 538's ELO. The biggest difference at 
the moment, I believe, is that I don't account for if a team is playing at home
or away.

For information on what ELO is : https://fivethirtyeight.com/features/introducing-nfl-elo-ratings/


Sample output of program on 10/4/2017:

```                      
team                    wins  losses  Current ELO                                           
Kansas City Chiefs       4       0         1681
New England Patriots     2       2         1657
Atlanta Falcons          3       1         1631
Pittsburgh Steelers      3       1         1612
Green Bay Packers        3       1         1604
Denver Broncos           3       1         1582
Detroit Lions            3       1         1559
Seattle Seahawks         2       2         1558
Dallas Cowboys           2       2         1556
Buffalo Bills            3       1         1541
Philadelphia Eagles      3       1         1535
Carolina Panthers        3       1         1534
New Orleans Saints       2       2         1525
Oakland Raiders          2       2         1517
Washington Redskins      2       2         1515
Minnesota Vikings        2       2         1510
Houston Texans           2       2         1508
Arizona Cardinals        2       2         1501
Tampa Bay Buccaneers     2       1         1500
Cincinnati Bengals       1       3         1478
Baltimore Ravens         2       2         1465
New York Giants          0       4         1463
Los Angeles Rams         3       1         1455
New York Jets            2       2         1454
Miami Dolphins           1       2         1450
Tennessee Titans         2       2         1450
Indianapolis Colts       1       3         1435
Jacksonville Jaguars     2       2         1433
Los Angeles Chargers     0       4         1407
Chicago Bears            1       3         1370
San Francisco 49ers      0       4         1319
Cleveland Browns         0       4         1292
```