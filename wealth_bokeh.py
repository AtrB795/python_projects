import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, output_file, save
from bokeh.io import curdoc
import bokeh.colors.hsl
from bokeh.models import CategoricalColorMapper
from bokeh.models import ColumnDataSource
from bokeh.palettes import d3
from bokeh.models import HoverTool
from bokeh.models.widgets import Panel, Tabs



covid = pd.read_csv('My_covid_project_data.csv')

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
covid_pivoted['sizes'] = [2 if cases < 5000 else 4 if cases < 10000 else 6 if cases < 15000 else 8 if cases < 20000 else 12 if cases < 25000 else 14 if cases < 30000 else 16 if cases < 35000 else 18 for cases in covid_pivoted['total_cases']]
covid_pivoted['continent'] = [index[1] for index in covid_pivoted.index]
covid_pivoted['iso_code'] = [index[0] for index in covid_pivoted.index]
hover = HoverTool(tooltips=[('Country','@iso_code'), ('Cases', '@total_cases')])
source = ColumnDataSource(covid_pivoted)
pal=d3['Category10'][len(covid_pivoted['continent'].unique())]
color_mapper = CategoricalColorMapper(factors=covid_pivoted['continent'].unique(), palette=pal)
fig = figure(x_axis_label='total_tests_per_thousand', y_axis_label='total_cases_per_million', tools='box_select,lasso_select,pan,wheel_zoom,box_zoom')
fig.circle(source=source, x='total_tests_per_thousand', y='total_cases_per_million', color={'field':'continent', 'transform':color_mapper}, legend='continent', selection_alpha=1, nonselection_alpha=0.1, hover_alpha=0.5, alpha=1, size='sizes')
fig.add_tools(hover)


#------------------------------------------------------------------------------------------------------------------------------------------

hover2 = HoverTool(tooltips=[('Country','@location'), ('Death', '@total_deaths')])
pal=d3['Category10'][len(covid_pivoted['continent'].unique())]
color_mapper = CategoricalColorMapper(factors=covid_pivoted['continent'].unique(), palette=pal)
fig2 = figure(x_axis_label='aged_70_older', y_axis_label='total_deaths_per_million', tools='box_select,lasso_select,pan,wheel_zoom,box_zoom')
fig2.circle(source=source, x='aged_70_older', y='total_deaths_per_million', color={'field':'continent', 'transform':color_mapper}, legend='continent', selection_alpha=1, nonselection_alpha=0.1, hover_alpha=0.5, alpha=1, size='sizes')
fig2.add_tools(hover2)




#---------------------------------------------------------------------------------------------------------------------------------------------

tab1 = Panel(child=fig, title='total_tests_per_thousand vs total_cases_per_million')
tab2 = Panel(child=fig2, title='aged_70_older vs total_deaths_per_million')
layouts = Tabs(tabs=[tab1, tab2])

curdoc().add_root(layouts)
curdoc().title = 'asd'