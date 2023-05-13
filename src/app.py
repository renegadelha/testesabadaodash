from dash import Dash, html

app = Dash(__name__)
server = app.server #server heroku/render reconhecer a app

app.layout = html.Div( children=[
    html.H1('Meu primeiro projeto '),
    html.Div(
        html.A('os dias estao muito complexos devido ao problema de falta de luz')
    )
])

if __name__ == '__main__':
    app.run_server(debug= True)