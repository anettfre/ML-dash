import os
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


from sider import (
    predict
)

app = dash.Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

a = dbc.NavbarSimple(
    brand="Hei",
    brand_href="#",
    color="primary",
    dark=True,
)

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), a,
     html.Div(id="page-content", children=[])]
)


# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return predict.create_layout(app)
    else:
        return predict.create_layout(app)


@app.callback(Output('output-image-upload', 'children'),
              [Input('upload-image', 'contents')])
def update_output(list_of_contents):
    if list_of_contents is not None:
        children = [html.Img(id="her-er-bildet", src=list_of_contents,
                             className="svg-container", style={"max-width": "90%"})]
        return children


@app.callback(
    Output("tmp", "children"),
    [Input("upload-image", "contents")]
)
def bilde_til_fil(base_64_bilde):
    # print(base_64_bilde)
    return base_64_bilde


if __name__ == '__main__':
    app.run_server(debug=True)
