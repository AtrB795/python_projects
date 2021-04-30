import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()

covid = pd.read_csv('My_covid_project_data.csv')
covid.fillna(0)
sns.regplot(covid[covid['continent'] == 'Asia']['human_development_index'],
           covid[covid['continent'] == 'Asia']['life_expectancy'], color='r')
sns.regplot(covid[covid['continent'] == 'Africa']['human_development_index'],
           covid[covid['continent'] == 'Africa']['life_expectancy'], color='#E3E32B')
sns.regplot(covid[covid['continent'] == 'Europe']['human_development_index'],
           covid[covid['continent'] == 'Europe']['life_expectancy'], color='#43FDFF')
sns.regplot(covid[covid['continent'] == 'South America']['human_development_index'],
           covid[covid['continent'] == 'South America']['life_expectancy'], color='#0FFF09')
sns.regplot(covid[covid['continent'] == 'North America']['human_development_index'],
           covid[covid['continent'] == 'North America']['life_expectancy'], color='#2823FF')
sns.regplot(covid[covid['continent'] == 'Oceania']['human_development_index'],
           covid[covid['continent'] == 'Oceania']['life_expectancy'], color='#FF0FF2')
ax.set(xlabel='human development', ylabel='life expectancy', title='life expectancy vs human development')
sns.axes_style('dark')
plt.legend(['As', 'Afr', 'Eur', 'SouthA', 'NorthA', 'Oce'])
ax.axvline(x=covid['human_development_index'].mean(), color='#FF0C18', linestyle='--')
ax.axvline(x=0.854, color='b', linestyle='--')

plt.legend(['As', 'Afr', 'Eur', 'SouthA', 'NorthA', 'Oce'])


plt.show()
#plt.savefig('lifevs.jpg', dpi=300, bbox_inches='tight')
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(covid[covid['iso_code']=='HUN']['human_development_index'])
