import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, output_file, save
import bokeh
import bokeh.colors.hsl
from bokeh.models import CategoricalColorMapper
from bokeh.models import ColumnDataSource
from bokeh.palettes import d3
from bokeh.models import HoverTool
from bokeh.models.widgets import Panel, Tabs
from bokeh.layouts import widgetbox, row
from bokeh.models import Slider, Column

#CategoricalColorMapper, ColumnDataSource, HoverTool, Panel, Tabs
class My_data_vis_class():
    def __init__(self, csv_file='My_covid_project_data.csv', indexes=['iso_code', 'continent'], func=np.mean, pivot_it=True):
        df = pd.read_csv(csv_file)

        df_sorted = df.sort_index(ascending=True)
        df_pivoted = df_sorted.pivot_table(index=indexes, values=df_sorted.columns, aggfunc=func)
        for index, index_name in zip(range(len(indexes)), indexes):
            df_pivoted[index_name] = [ind[index] for ind in df_pivoted.index]
        if pivot_it==True:
            self.dataframe = df_pivoted
        else:
            self.dataframe = df#.fillna(0)
            self.pivot_it = pivot_it

    def scatter_bokeh(self, x, y, x_axis_label, y_axis_label, hue='continent', palette_category='Category10', tools='box_select,lasso_select,pan,wheel_zoom,box_zoom', source=None, x_range=None, y_range=None, maintime=None):
        if source == None and maintime == None:
            source = ColumnDataSource(data=self.dataframe)
            list_of_hues = list([str(k) for k in self.dataframe[hue].unique()])
            pal=d3[palette_category][len(list_of_hues)]
            color_mapper = CategoricalColorMapper(factors=list_of_hues, palette=pal)
        else:
            source=source
            list_of_hues = list([str(k) for k in self.dataframe.loc[maintime][hue].unique()])
            pal=d3[palette_category][len(list_of_hues)]
            color_mapper = CategoricalColorMapper(factors=list_of_hues, palette=pal)

        if x_range == None and y_range==None:
            fig = figure(x_axis_label=x_axis_label, y_axis_label=y_axis_label, tools=tools)
        else:
            fig = figure(x_axis_label=x_axis_label, y_axis_label=y_axis_label, tools=tools, x_range=x_range, y_range=y_range)
        fig.circle(source=source, x=x, y=y, color={'field':hue, 'transform':color_mapper}, legend=hue, selection_alpha=1, nonselection_alpha=0.1, hover_alpha=0.5, alpha=1)
        return fig


    #------------------------------------------------------------------------------------------------------------------------------------------

    def add_hover(self, figure, tooltips=[('Country', '@iso_code'), ('Cases', '@total_cases')]):
        hover = HoverTool(tooltips=tooltips)
        figure.add_tools(hover)
    #---------------------------------------------------------------------------------------------------------------------------------------------
    def add_tabs(self, figs, titles):
        if len(titles) == len(figs):
            tabs_list = [Panel(child=fig, title=title) for fig, title in zip(figs, titles)]
            layouts = Tabs(tabs=tabs_list)
            return layouts
        else:
            raise ValueError("The two list's length must be equalent")

    def slider_fig(self, x, y, hue='continent', palette_category='Category10', maintime=int(20200224)):
        if self.pivot_it==False:
            self.dataframe['maintime'] = [int(str(date).replace('-', '')) for date in self.dataframe['date']]
            #self.dataframe['maintime'] = self.dataframe['maintime'].fillna(int(20200224))
            self.dataframe.index = self.dataframe['maintime']
            self.source = ColumnDataSource(data={'x':self.dataframe.loc[maintime][x], 'y':self.dataframe.loc[maintime][y], hue:self.dataframe.loc[maintime][hue]})
            xmin, xmax = min(self.dataframe[x]), max(self.dataframe[x])
            ymin, ymax = min(self.dataframe[x]), max(self.dataframe[x])
            fig_for_slider = My_data_vis_class.scatter_bokeh(self, source=self.source, y='y', x='x', hue=hue, x_axis_label='x', y_axis_label='y', palette_category=palette_category, y_range=(ymin, ymax), x_range=(xmin, xmax), maintime=maintime)
            return fig_for_slider
        else:
            raise TypeError('You use the wrong function. Use the scatter_bokeh!')
    def slider_plot(self, fig, x, y, hue):
        def update_plot(attr, old, new):
            time = slider.value
            new_data = {'x' : self.dataframe.loc[time][x], 'y' : self.dataframe.loc[time][y], hue : self.datafram.loc[time][hue]}
            self.source.data = new_data





        slider = Slider(start=20200224, end=20210415, step=1, value=20200224, title='Time')
        slider.on_change('value', update_plot)
        layout = row(Column(slider), fig)
        return layout