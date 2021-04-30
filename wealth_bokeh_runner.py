import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, output_file, save
import bokeh
import bokeh.colors.hsl
from bokeh.models import CategoricalColorMapper, Slider
from bokeh.models import ColumnDataSource
from bokeh.palettes import d3
from bokeh.models import HoverTool
from bokeh.models.widgets import Panel, Tabs
from wealth_bokeh_oop import My_data_vis_class
from bokeh.layouts import widgetbox, row
from bokeh.io import curdoc



myclass = My_data_vis_class(pivot_it=False)
fig = myclass.slider_fig(x='total_tests_per_thousand', y='total_cases_per_million')#, maintime=int(20200224))
myclass.add_hover(figure=fig, tooltips=[('Country','@iso_code'), ('Death', '@total_deaths')])

fig2 = myclass.slider_fig(x='aged_70_older', y='total_deaths_per_million')#, maintime=int(20200224))
myclass.add_hover(figure=fig2, tooltips=[('Country','@iso_code'), ('Death', '@total_deaths')])

layout = myclass.slider_plot(fig, x='total_tests_per_thousand', y='total_cases_per_million', hue='continent')

#layout2 = myclass.slider_plot(fig, x='aged_70_older', y='total_deaths_per_million', hue='continent')
#show(layout)
#layouts = myclass.add_tabs(figs=[fig, fig2], titles=['tot_testvstot_cas', 'aged70vstot_death'])
myclass.dataframe.fillna(0)
output_file('oop1.html')

show(layout)
