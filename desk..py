


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
ax[0, 1].scatter(covid[covid['continent']=='Asia']['life_expectancy'], covid[covid['continent']=='Asia']['total_cases_per_million'], color='r')
ax[0, 1].scatter(covid[covid['continent']=='Africa']['life_expectancy'], covid[covid['continent']=='Africa']['total_cases_per_million'], color='#E3E32B')
ax[0, 1].scatter(covid[covid['continent']=='Europe']['life_expectancy'], covid[covid['continent']=='Europe']['total_cases_per_million'], color='#43FDFF')
ax[0, 1].scatter(covid[covid['continent']=='South America']['life_expectancy'], covid[covid['continent']=='South America']['total_cases_per_million'], color='#0FFF09')
ax[0, 1].scatter(covid[covid['continent']=='North America']['life_expectancy'], covid[covid['continent']=='North America']['total_cases_per_million'], color='#2823FF')
ax[0, 1].scatter(covid[covid['continent']=='Oceania']['life_expectancy'], covid[covid['continent']=='Oceania']['total_cases_per_million'], color='#FF0FF2')
ax[0, 1].set_xlabel('life_expectancy')
ax[0, 1].set_ylabel('total_cases_per_million')
ax[0, 1].set_title('life expectancy vs total cases per million')
plt.legend(['As', 'Afr', 'Eur', 'SouthA', 'NorthA', 'Oce'])



ax[1, 0].scatter(covid[covid['continent']=='Asia']['human_development_index'], covid[covid['continent']=='Asia']['people_vaccinated'], color='r')
ax[1, 0].scatter(covid[covid['continent']=='Africa']['human_development_index'], covid[covid['continent']=='Africa']['people_vaccinated'], color='#E3E32B')
ax[1, 0].scatter(covid[covid['continent']=='Europe']['human_development_index'], covid[covid['continent']=='Europe']['people_vaccinated'], color='#43FDFF')
ax[1, 0].scatter(covid[covid['continent']=='South America']['human_development_index'], covid[covid['continent']=='South America']['people_vaccinated'], color='#0FFF09')
ax[1, 0].scatter(covid[covid['continent']=='North America']['human_development_index'], covid[covid['continent']=='North America']['people_vaccinated'], color='#2823FF')
ax[1, 0].scatter(covid[covid['continent']=='Oceania']['human_development_index'], covid[covid['continent']=='Oceania']['people_vaccinated'], color='#FF0FF2')
ax[1, 0].set_xlabel('human development')
ax[1, 0].set_ylabel('people_vaccinated')
ax[1, 0].set_title('people vaccinated vs human development')
plt.legend(['As', 'Afr', 'Eur', 'SouthA', 'NorthA', 'Oce'])