import pandas as pd
import numpy as np


def populate_bats(lst, df):
    if lst[0] == 'Left':
        df['bats_L'] = 1
        df['bats_R'] = 0
    elif lst[0] == 'Right':
        df['bats_L'] = 0
        df['bats_R'] = 1
    else:
        df['bats_L'] = 0
        df['bats_R'] = 0
    return df


def find_data(lst):
    finalGame = ''
    for x in lst:
        if x.split()[0] == 'Bats:':
            bats = x.split()[1::3]
        if (x.split()[0][0].isnumeric()) and (int(x.split()[0][0]) != 2):
            height = int(x.split()[0][:-1].split('-')[0]) * 12 + int(x.split()[0][:-1].split('-')[1])
            weight = int(x.split()[1][:-2])
        if x.split()[0] == 'Debut:':
            debut = x.split()[1:4]
        if x.split()[0] == 'Last':
            finalGame = x.split()[2:5]
    return bats, height, weight, debut, finalGame


def check_eligibility(finalGame, df):
    temp_num = np.round((pd.Timestamp.now() - pd.to_datetime(' '.join(finalGame), infer_datetime_format=True)) / np.timedelta64(1, 'Y'), 2)
    if len(finalGame) == 0 or (temp_num < 5): 
        df['is_eligible'] = 0
    else:
        df['is_eligible'] = 1
    return df


def populate_allstar(soup, df):
    if soup.find('li', class_ = 'all_star') is None:
        df['ASGames'] = int(0)
    else:
        df['ASGames'] = int(soup.find('li', class_ = 'all_star').text.split()[0][:-1])
    return df


def populate_career_length(debut, finalGame, df):
    if len(finalGame) != 0:
        df['CareerLength'] = np.round((pd.to_datetime(' '.join(finalGame), infer_datetime_format=True) - pd.to_datetime(' '.join(debut), infer_datetime_format=True)) / np.timedelta64(1, 'Y'), 2)
    else:
        df['CareerLength'] = np.round((pd.Timestamp.now() - pd.to_datetime(' '.join(debut), infer_datetime_format=True)) / np.timedelta64(1, 'Y'), 2)
    return df