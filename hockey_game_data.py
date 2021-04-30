import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
hockey_data = pd.read_csv('game.csv')
pd.set_option("display.max_rows", None, "display.max_columns", None)
crosstab_for_heatmap = pd.crosstab(hockey_data, row=['away_goals'], col=['home_goals'])
sns.heatmap[crosstab_for_heatmap]
print(hockey_data.head())