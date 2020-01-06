import os
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


a=html.Div()


def create_layout(app):
    return html.Div([
        html.Div(a),
        html.Div([
            dcc.Upload(
                id='upload-image',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    # 'margin': '10px'
                },
                #className="row chart-top-bar",
                # Allow multiple files to be uploaded
                multiple=False
            ),
            html.Div(id='output-image-upload',
                     style={
                         "display": "flex",
                         'borderWidth': '1px',
                         'borderStyle': 'solid',
                         "justify-content": "center"}),
            html.P(id="tmp")],
            style={"display": "flex", "flex-direction": "column"},
            className="six columns")
    ])
