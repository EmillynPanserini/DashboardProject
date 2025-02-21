#
# from dash import Dash, html, dcc, Input, Output
# import plotly.express as px
# import pandas as pd
#
# app = Dash(__name__)
#
# # Criação de gráficos
#
# df = pd.read_excel('vendas_teste.xlsx')
#
# fig = px.bar(df, x='Estado Destino', y='Total Bruto', color='Estado Destino', barmode='group')
# opcoes = list(df['Estado Destino'].unique())
# opcoes.append('Todos os estados')
#
# app.layout = html.Div(children=[
#     html.H1(children='Dashboard Vendas'),
#
#     html.Div(children='''
#         Esse gráfico mostra a quantidade de total bruto por estado.
#     '''),
#     html.Div(id='texto'),
#
#     dcc.Dropdown(opcoes, value='Todos os estados', id='lista_estados'),
#
#     dcc.Graph(
#         id='grafico_quantidade_total_bruto',
#         figure=fig
#     )
# ])
#
# @app.callback(
#     Output('grafico_quantidade_total_bruto', 'figure'),
#     Input('lista_estados', 'value')
# )
# def update_output(value):
#     if value == "Todos os estados":
#         fig = px.bar(df, x='Estado Destino', y='Total Bruto', color='Estado Destino', barmode='group')
#     else:
#         tabela_filtrada = df.loc[df['Estado Destino'] == value, :]
#         print(f"Filtrado para {value}: {tabela_filtrada.shape}")
#         fig = px.bar(tabela_filtrada, x='Estado Destino', y='Total Bruto', color='Estado Destino', barmode='group')
#
#     return fig
#
# if __name__ == '__main__':
#     app.run_server(debug=True)