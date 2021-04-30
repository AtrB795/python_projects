import pandas as pd
import bokeh.plotting as bpl
import bokeh.models as bmo
from bokeh.palettes import d3
import bokeh.io as boi
#bpl.output_notebook()

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

covid_indexed = covid.set_index(['iso_code'])
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
covid_pivoted['continent'] = [index[1] for index in covid_pivoted.index]
source = bpl.ColumnDataSource(covid_pivoted)

# use whatever palette you want...
palette = d3['Category10'][len(covid_pivoted['continent'].unique())]
color_map = bmo.CategoricalColorMapper(factors=covid_pivoted['continent'].unique(),
                                   palette=palette)

# create figure and plot
p = bpl.figure()
p.scatter(x='total_tests_per_thousand', y='total_cases_per_million',
          color={'field': 'continent', 'transform': color_map},
          legend_label='continent', source=source)
boi.output_file('allatok.html')
bpl.show(p)