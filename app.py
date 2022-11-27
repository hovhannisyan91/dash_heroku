import dash
from dash import html, dcc

app = dash.Dash(__name__, use_pages=True)
server=app.server
app.layout = html.Div(
    [
        html.Div([
            dcc.Link(html.Button(page['name'], id="navigation"), href=page['path'])
            for page in dash.page_registry.values()
        ], className="twelve columns"),
        html.Hr(),

        # content of each page
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run(debug=True)

