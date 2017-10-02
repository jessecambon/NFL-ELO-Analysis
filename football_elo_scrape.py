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


# Data source
data_url = 'https://www.pro-football-reference.com/years/2017/games.htm#games::none'
         

# Scrape the index of a given page
# Return a list of the links
def scrape(selection,element_type):

    
    # Select the given div
  #  data = soup.findAll("div", { "class" : "table_outer_container" })
    
    list_links = []
    data = soup.findAll("td", { "data-stat" : selection })
    for element in data:
        #print(element['href'])
        links = element.findAll(element_type)
        list_links += [a.contents[0] for a in links]
        #print(list_links)
   # 
    return list_links




page = requests.get(data_url)
soup = BeautifulSoup(page.content, 'html.parser')


# Automatically only goes as far as shortest list
# which is the pts_win (limits to only current games played)

# this is a game level dataframe
season = pd.DataFrame(list(zip(scrape("winner",'a'),scrape("loser",'a'),scrape("pts_win",'strong')))
    ,columns=['winner','loser',"pts_win"])


# This is a team level dataframe
# I append winners to losers to get all possible teams
team_ref = pd.DataFrame(season['winner'].append(season['loser']),columns=['team']).drop_duplicates().set_index(['team'])

#initialize vars

#team_ref['elo'] = 1500
team_ref['elo'] = [[1500] for _ in range(len(team_ref))]


# Initialize wins
team_ref['wins'] = 0
team_ref['losses'] = 0


# ELO rating day of the match
season['winner_elo'] = 0
season['loser_elo'] = 0
season['elo_diff'] = 0

# ELO rating adjusted for the given match results
season['winner_adj_elo'] = 0
season['loser_adj_elo'] = 0
season['elo_adj_diff'] = 0


# Change the Elo of a team using the index (index is the team name)


K = 20 # this is the ELO adjustment constant

for i in range(len(season)):
    
    # Names of teams that won and lost for a given game
    winner = season.loc[i]['winner']
    loser = season.loc[i]['loser']
    
    
    
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
    expected_loser_score = trans_loser_rating / (trans_winner_rating + trans_loser_rating)
    
    season.at[i,'winner_adj_elo'] = season.at[i,'winner_elo'] + K * (1 - expected_winner_score)
    season.at[i,'loser_adj_elo'] = season.at[i,'loser_elo'] + K * (0 - expected_loser_score)
    season.at[i,'elo_adj_diff'] = season.at[i,'winner_adj_elo'] - season.at[i,'loser_adj_elo']
    
    # Add our new elo scores to the team level spreadsheet
    
    team_ref.at[winner,'elo'].append(season.at[i,'winner_adj_elo'])
    team_ref.at[loser,'elo'].append(season.at[i,'loser_adj_elo'])
    
    #team_ref.loc[team_ref.loc[winner], 'wins'] += 1
    
# Adds a given value to an elo rating
#team_ref.at['New York Giants','elo'].append(team_ref.at['New York Giants','elo'][-1] + 5)
    
 
#team_ref['elo'][-1]

team_ref['Current ELO'] = [ a[-1] for a in team_ref['elo'] ]


# Display teams with the top ELOS
print(team_ref[['wins','losses','Current ELO']].sort_values('Current ELO',ascending=False))

#team_ref.loc['Chicago Bears']['elo'] += 500
    
    

#team_ref.sort_values('wins',ascending=False)



#download_file('https://energyplus.net/weather-location/africa_wmo_region_1/EGY//EGY_Asyut.623930_ETMY/weather-download/africa_wmo_region_1/EGY//EGY_Asyut.623930_ETMY/EGY_Asyut.623930_ETMY.epw','Weather Files')

#import re

# Initialize index
#Index = pd.DataFrame(columns=['Region','Country','City','Filename']) # Create empty dataframe
    
#scrape_links(data_url): # Regions

