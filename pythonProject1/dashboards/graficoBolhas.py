from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel('compras_teste.xlsx')

df_grouped = df.groupby(['Estado Destino', 'Estado Origem'], as_index=False)['Total Bruto'].sum()

opcoes_destino = list(df['Estado Destino'].unique())
opcoes_destino.append('Todos os estados de destino')
opcoes_graficos = ['Barras Verticais', 'Barras Horizontais', 'Pizza', 'Dispersão']

app.layout = html.Div([
    html.H1('Dashboard compras'),
    html.Div('Escolha o estado de destino e o tipo de gráfico para visualizar os estados.'),
    dcc.Dropdown(opcoes_destino, value='Todos os estados de destino', id='lista_destino'),
    dcc.Dropdown(opcoes_graficos, value='Barras Verticais', id='tipo_grafico'),
    dcc.Graph(id='grafico_quantidade_total_bruto')
])

@app.callback(
    Output('grafico_quantidade_total_bruto', 'figure'),
    [Input('lista_destino', 'value'), Input('tipo_grafico', 'value')]
)
def update_output(destino, tipo_grafico):
    # Filtrar os dados com base no estado de destino
    if destino == "Todos os estados de destino":
        df_filtrado = df_grouped
        title = 'Estados de Origem que Mais Vendem (Todos os Estados de Destino)'
    else:
        df_filtrado = df_grouped[df_grouped['Estado Destino'] == destino]
        title = f'Estados de Origem que Mais Vendem para {destino}'

    df_filtrado = df_filtrado.sort_values('Total Bruto', ascending=False)

    if not df_filtrado.empty:
        maior_vendedor = df_filtrado.iloc[0]['Estado Origem']
        maior_valor = df_filtrado.iloc[0]['Total Bruto']
    else:
        maior_vendedor = 'Nenhum'
        maior_valor = 0

    if tipo_grafico == 'Barras Verticais':
        fig = px.bar(
            df_filtrado,
            x='Estado Origem',
            y='Total Bruto',
            color='Estado Origem',
            title=title,
            text=df_filtrado['Total Bruto'].apply(lambda x: f'{x:,.2f}')  # Mostrar valores nas barras
        )
        fig.update_traces(textposition='auto')  # Posicionar os valores
    elif tipo_grafico == 'Barras Horizontais':
        fig = px.bar(
            df_filtrado,
            y='Estado Origem',
            x='Total Bruto',
            color='Estado Origem',
            orientation='h',
            title=title,
            text=df_filtrado['Total Bruto'].apply(lambda x: f'{x:,.2f}')
        )
        fig.update_traces(textposition='auto')
    elif tipo_grafico == 'Pizza':
        fig = px.pie(
            df_filtrado,
            names='Estado Origem',
            values='Total Bruto',
            title=title
        )
        fig.update_traces(textinfo='percent+label')  
    elif tipo_grafico == 'Dispersão':
        fig = px.scatter(
            df_filtrado,
            x='Estado Origem',
            y='Total Bruto',
            color='Estado Origem',
            size='Total Bruto',
            title=title
        )

    # Personalizar o layout e adicionar anotação com o maior vendedor
    fig.update_layout(
        showlegend=False,  # Remover legenda redundante
        title={'text': title, 'x': 0.5, 'xanchor': 'center'},
        annotations=[
            dict(
                text=f'Maior vendedor: {maior_vendedor} ({maior_valor:,.2f})',
                xref="paper", yref="paper",
                x=0.95, y=1.05, showarrow=False,
                font=dict(size=12)
            )
        ]
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)