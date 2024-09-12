import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP,
    "https://fonts.googleapis.com/css2?family=Jost:wght@300;400;700&display=swap",  # Jost is very similar to Futura
],
                title="Pian8")

# Custom styles
custom_style = {
    'fontFamily': "'Jost', sans-serif",
}


# Define the layout
app.layout = dbc.Container([
    html.Link(
        rel='stylesheet',
        href='https://fonts.googleapis.com/css2?family=Jost:wght@300;400;700&display=swap'
    ),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Img(src="/assets/banner.png", className="img-fluid rounded"),
            ], className="text-center"),
            html.H2("Join me for live piano performances!", 
                    className="text-center mt-4 mb-4",
                    style={'fontFamily': "'Jost', sans-serif", 'fontWeight': '400'}),
            html.Div([
                dbc.Button("Watch on Twitch", color="dark", className="mb-3 w-100", href="https://www.twitch.tv/pian8"),
                dbc.Button("Donate", color="dark", className="mb-3 w-100", href="https://www.justgiving.com/page/pian8"),
                dbc.Button("Song List", color="dark",  className="w-100", href="https://www.streamersonglist.com/t/pian8/songs"),
            ], className="d-flex flex-column align-items-center", style={"max-width": "200px", "margin": "0 auto"})
        ], width=8, className="mx-auto")
    ])
], fluid=True, style=custom_style)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)