import pickle
import numpy as np
import streamlit as st
from src.player_scraping import gather_player_data, standarize_data


with open('./pickle/improved_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('./pickle/player_lookup_df.pkl', 'rb') as f:
    player_look_up = pickle.load(f)


option = st.selectbox('Enter the name of a current MLB player!', player_look_up['Name'], index=0) # gives the dropdown menu based on the names in player_look_up

player_ID = player_look_up.loc[player_look_up['Name'] == option]['playerID'].to_string().split()[1] # after selecting a player, it finds the player_ID of the player within player_look_up

player_percent = np.round(model.predict_proba(standarize_data(gather_player_data(player_ID)))[0][1] * 100, 2) # uses the model to predict the HOF chances of the player

st.subheader('Hall of Fame Chances:')
st.title(str(player_percent) + '%')

## TODO: add file to do the stuff below, include graphs!!

st.write(gather_player_data(player_ID).drop(['SO', 'bats_L', 'bats_R', 'CST', 'SF', 'height', 'weight'], axis=1))
top_4 = standarize_data(gather_player_data(player_ID)).drop(['SO', 'bats_L', 'bats_R', 'CST'], axis=1) 
top_4_final = top_4.T.iloc[:, 0].sort_values(ascending=False)[:4] # finds the top 4 stats of the player based on their percentile
top_4_cols = top_4_final.index # gets the stats names of the top 4

st.write('Top 4 Percentile Ranks')

col1, col2, col3, col4 = st.columns(4)
col1.metric(label=top_4_cols[0], value=int(np.round(top_4_final[0], 2) * 100))
col2.metric(label=top_4_cols[1], value=int(np.round(top_4_final[1], 2) * 100))
col3.metric(label=top_4_cols[2], value=int(np.round(top_4_final[2], 2) * 100))
col4.metric(label=top_4_cols[3], value=int(np.round(top_4_final[3], 2) * 100))

