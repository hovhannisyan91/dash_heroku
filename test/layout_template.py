from dash import html, dcc, Dash, dash_table
from dash.dependencies import Input, Output, State
import base64



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
			dcc.Dropdown(id='image-picker',
						options=[
							{'label':'image1','value':'image1.jpg'},
							{'label':'image2','value':'image2.jpg'}
						],
						value='image2.jpg',                
						multi=False),
			
			dcc.Graph(id='some-graph')
		], className="seven columns"),
		html.Div([
			html.Img(id="image")	
		], className="five columns")
	], className="twelve columns"),

	html.Hr(),



], className='twelve columns')

#----------------Callbacks----------------------------#
@app.callback(Output('image','src'),
			[Input('image-picker','value')]
			)

def update_pic(value):
	img=str(value)
	encoded_image = base64.b64encode(open(value, 'rb').read()) # rb means reading binary
	img='data:image/jpg;base64,{}'.format(encoded_image.decode()) # decoding
	return img

if __name__=='__main__':
	app.run_server(debug=True, port=8055)