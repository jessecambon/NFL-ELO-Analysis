# -*- coding: utf-8 -*-
"""
Created on 10/2/2017 

@author: Jesse Cambon
"""


### Goal of this program is to calculate ELO for an NFL season
# by scraping results off of a website.

# There is a result level dataframe and a team level dataframe
# ELOs are adjusted for each result and then stored in the team level dataframe


# 10/2/2017: Currently this just calculates ELO for historical results


from bs4 import BeautifulSoup
#import urllib.request
import requests
import pandas as pd


# Calculate ELO rating for NFL teams using data scraped from web
# Starting out with calculating # of wins


# Data source we are going to scrape for results
data_url = 'https://www.pro-football-reference.com/years/2017/games.htm#games::none'
         

# Scrape the index of a given page
# Return a list of specified web elements
def scrape(selection,element_type):

    
    # Select the given div
  #  data = soup.findAll("div", { "class" : "table_outer_container" })
    
    list_links = []
    data = soup.findAll("td", { "data-stat" : selection })
    for element in data:
        #print(element['href'])
        
        # Add NA option 
        if element_type!='na':          
            list_links += [a.contents[0] for a in element.findAll(element_type)]
        else:
            # Extracts number if it exists
            if str(element.renderContents()) != "b''":
                list_links += [str(element.renderContents()).split('\'')[1]]
        #print(list_links)
   # 
    return list_links



# This is the web data we 
page = requests.get(data_url)
soup = BeautifulSoup(page.content, 'html.parser')


# Automatically only goes as far as shortest list
# which is the pts_win (limits to only current games played)
import numpy as np
# this is a game level dataframe

length = len(scrape("pts_win",'strong'))

season = pd.DataFrame(np.column_stack([scrape("winner",'a')[:length],scrape("loser",'a')[:length],scrape("pts_win",'strong')[:length],scrape("pts_lose",'na')[:length]]),columns=['winner','loser',"pts_win",'pts_lose'])

season['pts_diff'] = season['pts_win'].astype(int) - season['pts_lose'].astype(int)

# This is a team level dataframe
# I append winners to losers to get all possible teams
team_ref = pd.DataFrame(season['winner'].append(season['loser']),columns=['team']).drop_duplicates().set_index(['team']).sort_index()

#initialize vars


# Typed these values in from 538.com
# teams in alphabetical order
elo_list = [
[    1537],
[    1617],
[    1491],
[    1484],
[    1527],
[    1384],
[    1516],
[    1336],
[    1569],
[    1556],
[    1501],
[    1587],
[    1502],
[    1514],
[    1382],
[    1613],
[    1437],
[    1399],
[    1509],
[    1498],
[    1687],
[    1498],
[    1530],
[    1452],
[    1530],
[    1511],
[    1599],
[    1353],
[    1571],
[    1506],
[    1460],
[    1504]]

team_ref['elo'] = elo_list

# Old code to start every team at 1500
#team_ref['elo'] = [[1500] for _ in range(len(team_ref))]


# Initialize wins
team_ref['wins'] = 0
team_ref['losses'] = 0


# Initialize ELO rating day of the match
season['winner_elo'] = 0
season['loser_elo'] = 0
season['elo_diff'] = 0

# Initialize ELO rating adjusted for the given match results
season['winner_adj_elo'] = 0
season['loser_adj_elo'] = 0
season['elo_adj_diff'] = 0


# Change the Elo of a team using the index (index is the team name)


K = 20 # this is the ELO adjustment constant


# Iterate through results of the season

for i in range(len(season)):
    
    # Names of teams that won and lost for a given game
    winner = season.loc[i]['winner']
    loser = season.loc[i]['loser']
    pts_diff = season.loc[i]['pts_diff']
    
    
    # Update counter on team sheet
    team_ref.at[winner,'wins'] += 1
    team_ref.at[loser,'losses'] += 1
    
    
    # Set starting ELO
    
    season.at[i,'winner_elo'] = team_ref.at[winner,'elo'][-1]
    season.at[i,'loser_elo'] = team_ref.at[loser,'elo'][-1]
    season.at[i,'elo_diff'] = season.at[i,'winner_elo'] - season.at[i,'loser_elo']
    
    # Calculate Adjusted ELO
    # https://metinmediamath.wordpress.com/2013/11/27/how-to-calculate-the-elo-rating-including-example/
    trans_winner_rating = 10**(season.at[i,'winner_elo'] / 400)
    trans_loser_rating = 10**(season.at[i,'loser_elo'] / 400)
    
#    print(trans_winner_rating)
   # print(trans_loser_rating)
    
    expected_winner_score = trans_winner_rating / (trans_winner_rating + trans_loser_rating)
    
    elo_adj = np.log(pts_diff) * K * (1 - expected_winner_score)
    
    #expected_loser_score = trans_loser_rating / (trans_winner_rating + trans_loser_rating)
    
    season.at[i,'winner_adj_elo'] = season.at[i,'winner_elo'] + elo_adj
    season.at[i,'loser_adj_elo'] = season.at[i,'loser_elo'] - elo_adj
    season.at[i,'elo_adj_diff'] = season.at[i,'winner_adj_elo'] - season.at[i,'loser_adj_elo']
    
    # Add our new elo scores to the team level spreadsheet
    
    team_ref.at[winner,'elo'].append(season.at[i,'winner_adj_elo'])
    team_ref.at[loser,'elo'].append(season.at[i,'loser_adj_elo'])
    
    #team_ref.loc[team_ref.loc[winner], 'wins'] += 1
    
# Adds a given value to an elo rating
#team_ref.at['New York Giants','elo'].append(team_ref.at['New York Giants','elo'][-1] + 5)
    
 
#team_ref['elo'][-1]


# Get the current ELO, it's the last one in the ELO column list for each team
team_ref['Current ELO'] = [ a[-1] for a in team_ref['elo'] ]


# Display teams with the top ELOS
print(team_ref[['wins','losses','Current ELO']].sort_values('Current ELO',ascending=False))


