# from dash import Dash, dcc, html, Input, Output
# import plotly.graph_objects as go
# import plotly.express as px
# import pandas as pd
#
# app = Dash(__name__)
# df = pd.read_excel('vendas_teste.xlsx')
#
# fig = px.bar(df, x='ICMS', y='Estado Destino', color='Estado Destino', orientation='h') # barmode as orientation
# opcoes = list(df['Estado Destino'].unique())
# opcoes.append('Todos os estados')
#
# app.layout = html.Div(children=[
#     html.H1(children='Dashboard Vendas'),
#
#     html.Div(children='''
#         Esse gráfico mostra os estados e suas respectivas arrecadações de ICMS.
#     '''),
#     html.Div(id='texto'),
#
#     dcc.Dropdown(opcoes, value='Todos os estados', id='lista_estados'),
#
#     dcc.Graph(
#         id='grafico_quantidade_ICMS',
#         figure=fig
#     )
# ])
#
#
# @app.callback(
#     Output('grafico_quantidade_ICMS', 'figure'),
#     Input('lista_estados', 'value')
# )
# def update_output(value):
#
#     if value == "Todos os estados":
#         fig = px.bar(df, x='ICMS', y='Estado Destino', color='Estado Destino', orientation='h') # barmode as orientation
#     else:
#         tabela_filtrada = df.loc[df['Estado Destino'] == value, :]
#         fig = px.bar(df, x='ICMS', y='Estado Destino', color='Estado Destino', orientation='h') # barmode as orientation
#
#     # customização
#     fig.update_layout(
#         yaxis={'title': 'Estados'},
#         xaxis={'title': 'ICMS'},
#         showlegend=False
#     )
#     return fig
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)