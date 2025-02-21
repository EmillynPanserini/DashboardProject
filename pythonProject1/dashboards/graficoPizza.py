# from dash import Dash, html, dcc, Input, Output
# import plotly.express as px
# import pandas as pd
#
# app = Dash(__name__)
#
# # Carregar os dados
# df = pd.read_excel('vendas_teste.xlsx')
#
# # Preparar os dados iniciais para o gráfico de pizza (soma do Total Bruto por Estado Destino)
# df_pie = df.groupby('Estado Destino', as_index=False)['Total Bruto'].sum()
#
# # Criar gráfico de pizza inicial
# fig = px.pie(df_pie, names='Estado Destino', values='Total Bruto', title='Distribuição do Total Bruto por Estado')
#
#
# app.layout = html.Div(children=[
#     html.H1(children='Dashboard Vendas'),
#
#     html.Div(children='''
#         Esse gráfico mostra a distribuição do total bruto por estado em formato de pizza.
#     '''),
#
#     html.Div(id='texto'),
#
#
#
#     dcc.Graph(
#         id='grafico_quantidade_total_bruto',
#         figure=fig
#     )
# ])
#
#
# def update_output(value):
#     if value == "Todos os estados":
#         # Usar todos os dados, agrupados por Estado Destino
#         df_pie = df.groupby('Estado Destino', as_index=False)['Total Bruto'].sum()
#         fig = px.pie(df_pie, names='Estado Destino', values='Total Bruto', title='Distribuição do Total Bruto por Estado')
#     else:
#         # Filtrar os dados para o estado selecionado
#         tabela_filtrada = df.loc[df['Estado Destino'] == value, :]
#         print(f"Filtrado para {value}: {tabela_filtrada.shape}")
#         # Para um único estado, o gráfico de pizza pode não fazer sentido com uma única fatia,
#         # mas podemos mostrar apenas aquele estado como 100% para consistência
#         df_pie_filtered = tabela_filtrada.groupby('Estado Destino', as_index=False)['Total Bruto'].sum()
#         fig = px.pie(df_pie_filtered, names='Estado Destino', values='Total Bruto', title=f'Total Bruto para {value}')
#
#     return fig
#
# if __name__ == '__main__':
#     app.run_server(debug=True)