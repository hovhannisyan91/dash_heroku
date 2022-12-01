import dash
from dash import html, dcc

app = dash.Dash(__name__, use_pages=True,suppress_callback_exceptions=True)
server=app.server
app.layout = html.Div(
    [
        html.Div([
            dcc.Link(html.Button(page['name'], className="navigation"), href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        # content of each page
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)

