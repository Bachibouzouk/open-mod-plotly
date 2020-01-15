# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import plotly.express as px
from dash.exceptions import PreventUpdate
df = pd.read_csv('data/children-per-woman-UN.csv').set_index('country_iso')
df_table = pd.read_csv('data/children-per-woman-UN.csv')

# loading external resources
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
options = dict(
    # external_stylesheets=external_stylesheets
)


def extract_country(country_iso):
    d ={'x': df.loc[country_iso].year, 'y': df.loc[country_iso].fertility, 'mode': 'lines+markers', 'name': df.loc[country_iso].country.unique()[0]}
    return d

myapp = dash.Dash(__name__, **options)

myapp.layout = html.Div(
    children=[
        html.H1(children='Hello Dash'),
        html.Div(children='''Dash: A web application framework for Python.'''),
        html.Div("Here is a div", id="example-div"),
        html.Div([
            html.Div('A', className='highlighted'),
            html.Div('B', className='')],
            className='horizontal'),
        # dash_table.DataTable(
        #     id='table',
        #     columns=[{"name": i, "id": i} for i in df_table.columns],
        #     data=df_table.to_dict('records'),
        #     style_table={
        #         'maxHeight': '300px',
        #         'overflowY': 'scroll'
        #     },
        #     # filter_action="native",
        #     # sort_action="native",
        #     # fixed_rows={'headers': True, 'data': 0}
        # ),
        html.Div(
            id='paragraph'
        ),
        dcc.Dropdown(
            id='country-select',
            options=[
                {'label': df.loc[i].country.unique()[0], 'value': i}
                for i in df.index.dropna().unique()
            ],
            multi=True,
        ),
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': df.loc['KOR'].year, 'y': df.loc['KOR'].fertility, 'type': 'bar', 'name': 'SF'},
                    {'x': df.loc['CHN'].year, 'y': df.loc['CHN'].fertility, 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ]
)


@myapp.callback(
    [
        Output(component_id='paragraph', component_property='children'),
        Output(component_id='example-graph', component_property='figure')
    ],
    [Input(component_id='country-select', component_property='value')]
)
def update_figure(countries):
    if countries is None:
        raise PreventUpdate
    else:
        print('in here')
        fig = {
            'data': [
                extract_country(country)
                for country in countries
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
        return countries, fig


if __name__ == '__main__':
    myapp.run_server(debug=True)
