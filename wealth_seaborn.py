import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, output_file
import bokeh


#fig, ax = plt.subplots()
covid = pd.read_csv('My_covid_project_data.csv')
# continent_raw = pd.DataFrame(covid[['continent', 'iso_code']])
# continent = continent_raw.pivot_table(index='iso_code', values=['continent'])
covid_filled = covid.fillna(0)

covid_indexed = covid_filled.set_index(['iso_code'])
covid_sorted = covid_indexed.sort_index(ascending=True)
covid_pivoted = covid_sorted.pivot_table(index=[covid_sorted.index, 'continent'], values=['location', 'date', 'total_cases', 'new_cases',
        'new_cases_smoothed', 'total_deaths', 'new_deaths',
        'new_deaths_smoothed', 'total_cases_per_million',
        'new_cases_per_million', 'new_cases_smoothed_per_million',
        'total_deaths_per_million', 'new_deaths_per_million',
        'new_deaths_smoothed_per_million', 'reproduction_rate', 'icu_patients',
        'icu_patients_per_million', 'hosp_patients',
        'hosp_patients_per_million', 'weekly_icu_admissions',
        'weekly_icu_admissions_per_million', 'weekly_hosp_admissions',
        'weekly_hosp_admissions_per_million', 'new_tests', 'total_tests',
        'total_tests_per_thousand', 'new_tests_per_thousand',
        'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
        'positive_rate', 'tests_per_case', 'tests_units', 'total_vaccinations',
        'people_vaccinated', 'people_fully_vaccinated', 'new_vaccinations',
        'new_vaccinations_smoothed', 'total_vaccinations_per_hundred',
        'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred',
        'new_vaccinations_smoothed_per_million', 'stringency_index',
        'population', 'population_density', 'median_age', 'aged_65_older',
        'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
        'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
        'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
        'life_expectancy', 'human_development_index'], aggfunc=np.mean)
#covid_pivoted_whole= covid_pivoted.merge(continent, on='iso_code')
covid_pivoted.fillna(0)
covid_pivoted['sizes'] = [20 if cases < 5000 else 40 if cases < 10000 else 60 if cases < 15000 else 80 if cases < 20000 else 100 if cases < 25000 else 120 if cases < 30000 else 140 if cases < 35000 else 160 for cases in covid_pivoted['total_cases']]
#for hdi in covid['human_development_index']:
       #for life_expt in covid['life_expectancy']:
              #for cont in covid['continent']:
              #hdi_use = pd.DataFrame({'hdi':hdi})
              #life_expt_use = pd.DataFrame({'life_expct':life_expt})
#
# sns.jointplot(data=covid_pivoted_whole, x='human_development_index', y='life_expectancy', hue='continent', kind='scatter', size='sizes')






#sns.jointplot(data=covid, x='human_development_index', y='total_deaths_per_million', hue='continent', kind='scatter', ylim=(-1, 1500), xlim=(-1, 1.0))
#sns.jointplot(data=covid_pivoted, x='aged_70_older', y='total_deaths_per_million', hue='continent', kind='scatter')
#sns.jointplot(data=covid_pivoted, x='people_vaccinated_per_hundred', y='new_deaths_per_million', hue=covid_pivoted.index[1], kind='scatter', ylim=(-1, 7), xlim=(-1, 20))
sns.relplot(data=covid_pivoted, x='total_tests_per_thousand', y='total_cases_per_million', kind='scatter', hue='continent', size='total_cases', sizes=(40, 400)) #, ylim=(-1, 60000), xlim=(-1, 1500),
#covid_pivoted['colors'] = [ for coninent in covid_pivoted['continent']]
#p = figure(x_axis_label='total_tests_per_thousand', y_axis_label='total_cases_per_million', tools='box_select')


plt.show()

#pd.set_option("display.max_rows", None, "display.max_columns", None)
              #filled_continent = covid['continent'].fillna('0')
print(covid['continent'])   #[filled_continent['continent']=='0']