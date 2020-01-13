# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# loading external resources
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
options = dict(
    # external_stylesheets=external_stylesheets
)

demo_app = dash.Dash(__name__, **options)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
