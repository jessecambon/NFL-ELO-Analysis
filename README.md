# NFL ELO Analysis

Author: Jesse Cambon, myfullname -a/t- gmail


Date: 10/2/2017

Description:

Scrapes NFL results from pro-football-reference and calculates ELO ratings for each team.

Currently this is just for historical results. I also start ELOs at 1500 for the season
(does not take into account prior season)

For information on what ELO is : https://fivethirtyeight.com/features/introducing-nfl-elo-ratings/



Sample output of program on 10/2/2017:

```                      
team                  wins  losses  Current ELO                                  
Kansas City Chiefs       3       0         1528
Buffalo Bills            3       1         1520
Detroit Lions            3       1         1519
Carolina Panthers        3       1         1518
Pittsburgh Steelers      3       1         1518
Denver Broncos           3       1         1518
Green Bay Packers        3       1         1518
Los Angeles Rams         3       1         1518
Atlanta Falcons          3       1         1518
Philadelphia Eagles      3       1         1517
Washington Redskins      2       1         1510
Tampa Bay Buccaneers     2       1         1507
New Orleans Saints       2       2         1501
New York Jets            2       2         1500
Seattle Seahawks         2       2         1500
Houston Texans           2       2         1500
Arizona Cardinals        2       2         1499
Tennessee Titans         2       2         1499
New England Patriots     2       2         1499
Minnesota Vikings        2       2         1499
Dallas Cowboys           2       2         1499
Baltimore Ravens         2       2         1498
Jacksonville Jaguars     2       2         1498
Oakland Raiders          2       2         1498
Miami Dolphins           1       2         1487
Chicago Bears            1       3         1481
Indianapolis Colts       1       3         1480
Cincinnati Bengals       1       3         1480
Los Angeles Chargers     0       4         1462
Cleveland Browns         0       4         1460
San Francisco 49ers      0       4         1460
New York Giants          0       4         1460
```