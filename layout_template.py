from dash import html, dcc, Dash, dash_table
from dash.dependencies import Input, Output, State
import base64
import pandas as pd

ranges=pd.read_csv("data/ranges.csv")

app=Dash(__name__)
server=app.server
app.title = 'Div Template'
	
app.layout = html.Div([
	html.H1('Div Structure'),
	html.Hr(),
	# This div contains input forms and submit button
	html.Div([
		# Block 1
		html.Div([
			dcc.Input(id='number',
						type='number',
						value=2
						),
			
			html.H3(id='text')
		], className="seven columns"),


		html.Div([
			html.Img(id="image")	
		], className="five columns")
	], className="twelve columns"),

	html.Hr(),
	


], className='twelve columns')

#----------------Callbacks----------------------------#

@app.callback(Output('image','src'),
				Output('text','children'),
				[Input('number','value')]
			)

def update_pic(value):
	#look up the value
	checking = lambda row: row['low']<=value<=row['high']
	result = ranges[ranges.apply(checking, axis=1)==True]
	img=result['img'].values[0]
	text=result['t'].values[0]
	encoded_image = base64.b64encode(open(img, 'rb').read()) # rb means reading binary
	img='data:image/jpg;base64,{}'.format(encoded_image.decode()) # decoding
	return img, text


if __name__=='__main__':
	app.run_server(debug=True, port=8055)