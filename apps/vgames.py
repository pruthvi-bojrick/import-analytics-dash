import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

dfv = pd.read_csv(DATA_PATH.joinpath("importsConsumptionAIR_CNT.csv"))  # GregorySmith Kaggle
sales_list = ["NAICS 3 Consumption Imports by Air & Container"]


layout = html.Div([
    html.H1('Video Games Sales', style={"textAlign": "center"}),

    html.Div([
        html.Div(dcc.Dropdown(
            id='genre-dropdown', value='Strategy', clearable=False,
            options=[{'label': x, 'value': x} for x in sorted(dfv['NAICS_SDESC'].unique())]
        ), className='six columns'),

        html.Div(dcc.Dropdown(
            id='sales-dropdown', value='EU Sales', clearable=False,
            persistence=True, persistence_type='memory',
            options=[{'label': x, 'value': x} for x in sales_list]
        ), className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-bar', figure={}),
])


@app.callback(
    Output(component_id='my-bar', component_property='figure'),
    [Input(component_id='genre-dropdown', component_property='value'),
     Input(component_id='sales-dropdown', component_property='value')]
)
def display_value():
    # dfv_fltrd = dfv[dfv['Genre'] == genre_chosen]
    # dfv_fltrd = dfv_fltrd.nlargest(10, sales_chosen)
    # fig = px.bar(dfv_fltrd, x='Video Game', y=sales_chosen, color='Platform')
    fig = px.bar(dfv, x="NAICS_SDESC", y=['AIR_VAL_MO','CNT_VAL_MO'], 
                        title="NAICS3 Consumption Imports by Air & Container 2022")
# fig.show()
    # fig = fig.update_yaxes(tickprefix="$", ticksuffix="M")
    return fig
