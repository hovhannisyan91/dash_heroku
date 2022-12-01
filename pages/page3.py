import dash

from dash import callback,Input, Output, State, dcc, html


dash.register_page(__name__)



layout = html.Div([
    
    html.Div(
        [
            html.Div([dcc.Input(id='my-input3', value="", type='text',placeholder="Type on page 3")], className="three columns"),
            html.Div([html.Button(id='submit-button3', n_clicks=0, children='Submit')], className="three columns")

        ], className="six columns"
    ),
    
    html.Div(html.Div([html.P(id='my-output3')],className='my-output'), className="twelve columns")

], className='twelve columns')

#--------------------------------------------#
@callback(
    Output(component_id='my-output3',component_property='children'),
    [Input(component_id= 'submit-button3',component_property='n_clicks')],
    [State('my-input3','value')]
)
def update_output_div(n_clicks,input_value):
    return "Input: {0} \n Number of clicks:{1}".format(input_value,n_clicks)
