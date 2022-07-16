from dash import html, dcc, Dash, dash_table
from dash.dependencies import Input, Output, State
from datetime import datetime as dt, timedelta
import plotly.express as px

from components.figures import df
import pandas as pd

app=Dash(__name__)
app.title = 'Sample App'
    
app.layout = html.Div([
    
    html.Div([

        dcc.Dropdown(id='msize',
                        options=[{'label':i,'value':i} for i in df['MarketSize'].unique()],
                        value="Small"
                        )
    ], className="twelve columns"),

    html.Div(id='msize-output'),
    html.Hr(),

    html.Div([
       dcc.Dropdown(id='week',
                        options=[{'label':i,'value':i} for i in df['week'].unique()],
                        value=1
                        )
    ],className="twelve columns"),
    html.Div(id='week-output'),

    html.Div(id='display-table')


], className='twelve columns')

#--------------------------------------------#

@app.callback(Output('msize-output','children'),
                [Input('msize','value')])
def callback_a(msize):
    return "You have chosen {} market size".format(msize)

@app.callback(Output('week-output','children'),
                [   Input('week','value')])
def callback_b(week):
    return "You have chosen week: {}".format(week)

@app.callback(Output('display-table','children'),
                [Input('msize','value'),
                Input('week','value')])

def callback_df(msize,week):
    query=df[(df['MarketSize']==msize) & (df['week']==week)].groupby(['Promotion']).mean()['SalesInThousands']
    data=pd.DataFrame(query).reset_index()[['Promotion','SalesInThousands']]
    columns =  [{"name": i, "id": i,} for i in (data.columns)]
    return dash_table.DataTable(data=data.to_dict('records'), columns=columns)

if __name__=='__main__':
    app.run_server(debug=True)