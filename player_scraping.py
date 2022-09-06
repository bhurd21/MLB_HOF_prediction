import pandas as pd
import numpy as np

from src.career_standards_test import CST
from src.data_cleaning_functions import populate_bats, find_data, check_eligibility, populate_allstar, populate_career_length
from src.min_max import get_min_max

from bs4 import BeautifulSoup
import requests



def init_dataframe():
    df = pd.DataFrame(columns=['G', 'AB', 'R', 'H','2B', '3B', 'HR', 'RBI', 'SB', 'BB', 'SO', 'IBB', 'HBP', 'SF'])
    return df

def pop_df(bats, height, weight, debut, finalGame, soup, df):

    df['weight'] = weight
    df['height'] = height

    df = populate_career_length(debut, finalGame, df)
    df = check_eligibility(finalGame, df)
    df = populate_allstar(soup, df)
    df = populate_bats(bats, df)
    df = CST(df)

    return df



def gather_player_data(playerID):

#Get all data from the player's baseball reference page
    URL = 'https://www.baseball-reference.com/players/' + playerID[0] + '/' + playerID + '.shtml'
    text = requests.get(URL)
    soup = BeautifulSoup(text.content, 'lxml')

#Use bs to get all applicable raw numerical and categorical data
    num_data = []
    cat_data = []
    career_row = soup.find('tfoot').find('tr').find_all('td')
    bio_rows = soup.find_all('p')

#Get all numerical data from the career section of the player's stats section
    for stat in career_row:
        num_data.append(stat.text)

#Get required parts from the player's bio section to be parsed later
    for jobs in bio_rows:
        cat_data.append(jobs.text)
    cat_data = cat_data[:13]

#Organize numerical data
    df_num_data = []
    for num in [0, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 23, 20, 22]:
        df_num_data.append(int(num_data[num]))

    bats, height, weight, debut, finalGame = find_data(cat_data)

# Create DataFrame
    df = init_dataframe()
    df.loc[0] = df_num_data
    df = pop_df(bats, height, weight, debut, finalGame, soup, df)
# Reformat Columns
    df = df[['G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'BB', 'SO', 'IBB', 'HBP', 
            'SF', 'weight', 'height', 'bats_L', 'bats_R', 'CareerLength', 'ASGames', 'CST']]

    return df 

def standarize_data(df):

#Columns that log function will be applied to
    log_cols = ['G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'BB', 
    'SO', 'IBB', 'HBP', 'SF', 'CareerLength', 'ASGames', 'CST']

#Apply log function
    pts_temp = df
    for x in log_cols:
        pts_temp[x] = np.log(df[x] + 0.5)

#Columns that min_max will be applied to
    min_max_cols = ['G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'BB', 'SO', 
    'IBB', 'HBP', 'SF', 'weight', 'height', 'CareerLength', 'ASGames', 'CST']

#Get actual min_max values
    min_values, max_values = get_min_max()

#Apply min_max
    for x in range(19):
        df[min_max_cols[x]] = df[min_max_cols[x]] - min_values[x]
        df[min_max_cols[x]] = df[min_max_cols[x]] / max_values[x]

    return df