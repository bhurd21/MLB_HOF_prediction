import pickle
import pandas as pd
import numpy as np
import time
from datetime import datetime
from src.player_scraping import standarize_data, gather_player_data


def get_data():
    with open('./pickle/player_percentage_dic.pkl', 'rb') as f:
        player_dic = pickle.load(f)
    with open('./pickle/improved_model.pkl', 'rb') as f:
        model = pickle.load(f)

    player_IDs = ['freemfr01', 'altuvjo01', 'tatisfe02', 'machama01', 'perezsa02', 'sotoju01', 'yelicch01', 'buxtoby01']

    #player_dic = {"freemfr01": [], "altuvjo01": [], "tatisfe02": [], "machama01": [], "perezsa02": [], "sotoju01": [], "yelicch01": [], "buxtoby01": [], "date": []}

    for player in player_IDs:
        player_dic[player].append(np.round(model.predict_proba(standarize_data(gather_player_data(player))[0][1]) * 100, 6))
    todays_date = str(datetime.today()).split(' ')[0]
    player_dic['date'].append(todays_date)

    with open('player_percentage_dic.pkl','wb') as f:
        pickle.dump(player_dic,f)

if __name__ == "__main__":
    while True:
        get_data()
        print(datetime.today())
        days_in_between = 1
        time.sleep(days_in_between * 86400)
