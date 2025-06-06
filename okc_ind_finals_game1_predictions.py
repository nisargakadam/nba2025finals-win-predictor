# -*- coding: utf-8 -*-
"""okc_ind_finals_game1_predictions.ipynb


"""

pip install nba_api

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from nba_api.stats.endpoints import leaguegamefinder
#thunder game data
thunder = leaguegamefinder.LeagueGameFinder(team_id_nullable = '1610612760')

thunder_all = thunder.get_data_frames()[0]
thunder_all['GAME_DATE'] = pd.to_datetime(thunder_all['GAME_DATE'])
thunder2025 = thunder_all[thunder_all['GAME_DATE'] >= '2024-10-21'].copy()
thunder2025['WIN'] = thunder2025['WL'].apply(lambda x: 1 if x=='W' else 0)
thunder2025_sorted = thunder2025.sort_values('GAME_DATE')
#thunder2025_sorted = thunder2025_sorted[:-1]

#pacers game data
pacers = leaguegamefinder.LeagueGameFinder(team_id_nullable = "1610612754")

pacers_all= pacers.get_data_frames()[0]
pacers_all['GAME_DATE'] = pd.to_datetime(pacers_all['GAME_DATE'])
pacers2025 = pacers_all[pacers_all['GAME_DATE'] >= '2024-10-21'].copy()
pacers2025['WIN'] = pacers2025['WL'].apply(lambda x: 1 if x=='W' else 0)
pacers2025_sorted = pacers2025.sort_values('GAME_DATE')
#pacers2025_sorted = pacers2025_sorted[:-1]

thunder2025_sorted

metrics = ['FG_PCT', 'FG3_PCT', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PLUS_MINUS']

def playoffAverages(team, stats, n=18):
  return team.tail(n)[metrics].mean().round(2).to_dict()

thunder_avgs = playoffAverages(thunder2025_sorted, metrics, n=18)
pacers_avgs = playoffAverages(pacers2025_sorted, metrics, n=18)

thunder_avgs

X_thunder = thunder2025_sorted[metrics]
y_thunder = thunder2025_sorted['WIN']
thunder_scaler = StandardScaler()
X_thunderScaled = thunder_scaler.fit_transform(X_thunder)
thunderRF = RandomForestClassifier(random_state = 42)
thunderRF.fit(X_thunderScaled, y_thunder)



X_pacers = pacers2025_sorted[metrics]
y_pacers = pacers2025_sorted['WIN']
pacers_scaler = StandardScaler()
X_pacersScaled = pacers_scaler.fit_transform(X_pacers)
pacersRF = RandomForestClassifier(random_state = 42)
pacersRF.fit(X_pacersScaled, y_pacers)

#scale inputs

def input_lst(avgs, metrics):
  return np.array([[avgs[x] for x in metrics]])

thunderInput = input_lst(thunder_avgs, metrics)

pacersInput = input_lst(pacers_avgs, metrics)

def win_prob(teamModel, dataScaled):
  return teamModel.predict_proba(dataScaled)[0][1]

thunderProb = win_prob(thunderRF, thunderInput)

pacersProb = win_prob(pacersRF, pacersInput)

totalPercent = thunderProb + pacersProb

thunder_chance = thunderProb/totalPercent

pacers_chance = pacersProb/totalPercent

print("For Game 1 of the 2025 NBA Finals between the Oklahoma City Thunder and the Indiana Pacers, here are each team's chances of winning:")
print(f"Oklahoma City Thunder Chance of Winning: {round(thunder_chance *100, 2)}%")
print(f"Indiana Pacers Chance of Winning: {round(pacers_chance *100, 2)}%")



'''

For Game 1 of the 2025 NBA Finals between the Oklahoma City Thunder and the Indiana Pacers, here are each team's chances of winning:
Oklahoma City Thunder Chance of Winning: 50.79%
Indiana Pacers Chance of Winning: 49.21%

'''
