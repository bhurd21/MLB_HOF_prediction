# MLB_HOF_prediction
Uses popular python libraries such as pandas and scikit-learn to predict the chances of current Major League Baseball players to be inducted into the Hall of Fame.

** In order to fully replicate this project locally, you will need to download the baseball database I used, which can be found here **  https://www.seanlahman.com/baseball-archive/statistics 


MLB_HOF_predictor.ipynb - the main notebook I used for 80% of this project. Start here.

The other files are intended to be used for Streamlit, a popular web hosting data science platform. I will explain each file below:

MLB_HOF.py - the file that is run in Streamlit, the final product.

SRC folder: career_standards_test.py, data_cleaning_functions.py, min_max.py, player_scraping.py
- used by the MLB_HOF.py file to prep the scraped data for output to the user.

Pickle folder: improved_model.pkl, player_lookup.pkl, player_percentage_dic.pkl
- holds the model, all current players, and a dictionary to track a players chance of HOF induction over time, respectively.

collect_player_percentages.py - I used this to track a few current MLB players I was interested in at the time to see how the model reacted to their performaces each day. 
