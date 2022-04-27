from dash import html, dcc, Dash, dash_table
from dash.dependencies import Input, Output, State
from datetime import datetime as dt, timedelta
import plotly.express as px
import pandas_datareader.data as web
# from components.data import options
import pandas as pd

		
app=Dash(__name__)
app.title = 'Stock Ticker Dashboard'
	
app.layout = html.Div([
	html.H1('Stock Ticker Dashboard'),
	html.Hr(),
	# This div contains input forms and submit button
	html.Div([
		# Block 1
		html.Div([
			html.Label('Select Stock Symbol:'),
			dcc.Dropdown(id='stock-picker',
						options=[
							{'label':'Amazon','value':'AMZN'},
							{'label':'Apple','value':'AAPL'},
							{'label':'Google','value':'GOOG'},
							{'label':'Netflix','value':'NFLX'}
						],
						value=['GOOG'],                
						multi=True)
		], className="four columns"),
		# Block 2
		html.Div([
			html.Label('Select Start and End dates:'),
			dcc.DatePickerRange(
				id='date-range-picker',
				start_date=dt.today()-timedelta(days=14),
				end_date=dt.today(),
				max_date_allowed=dt.today() 
			)
		], className="four columns"),
		# Block 3
		html.Div([
			html.Button(id='submit-button', n_clicks=0, children='Submit')
		
		], className="four columns"),
	], className="twelve columns"),

	html.Hr(),

	html.Div([
		dcc.Graph(id='my-graph')
	], className="twelve columns"),

	html.Hr(),

	html.Div([ 
		html.Label("In this block we can have extra stuff")
	], className="twelve columns temp-div")

], className='twelve columns')

#----------------Callbacks----------------------------#
@app.callback(Output('my-graph','figure'),
			[Input('submit-button','n_clicks')],
			[State('stock-picker','value'),
			State('date-range-picker','start_date'),
			State('date-range-picker','end_date')   
			])

def update_graph(n_clicks,stock_ticker,start,end):
	data_source='yahoo'
	traces=[]
	for i in stock_ticker:
		df=web.DataReader(i,data_source,start,end).reset_index()
		df['Stock Name']=i
		traces.append(df)
	data=pd.concat(traces)
	fig = px.line(data, x="Date", y="Close", color='Stock Name', title="Stock Prices")
	return fig

if __name__=='__main__':
	app.run_server(debug=True, port=8055)