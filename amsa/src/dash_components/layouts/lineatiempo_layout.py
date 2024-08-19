from dash import html, dcc
import dash_bootstrap_components as dbc

def lineatiempo_layout():
    """
    Genera el diseño de la interfaz para el gráfico de líneas en la aplicación Dash.

    El diseño incluye:
    - Un título "Gráfico de Líneas".
    - Un selector de rango de fechas.
    - Dropdowns para seleccionar KPI, niveles y tipos de datos.
    - Un gráfico de líneas para mostrar los datos seleccionados.

    Returns:
        dbc.Container: Un contenedor de Dash Bootstrap Components que organiza los elementos de la interfaz.
    """
    
    return dbc.Container(
        [
            dbc.Row(  # Primera fila: Título "Gráfico de Líneas"
                dbc.Col(
                    html.Div(
                        [
                            html.Span("Gráfico de Líneas", style={'fontSize': '3rem', 'color': '#007993'}),
                        ]
                    ),
                ),
                style={'marginBottom': '5%'}
            ),
            dbc.Row(  # Segunda fila: Selector de fechas
                dbc.Col(
                    [
                        html.Div(
                            html.Span('Seleccionar Fecha', style={'color': '#8f8f8f'}),
                        ),
                        dcc.DatePickerRange(
                            id='lineas-date-picker',
                        ),
                    ],
                ),
                style={'marginBottom': '1%'}
            ),
            dbc.Row(  # Tercera fila: Selectores de KPI, niveles y tipos
                [
                    dbc.Col(
                        [
                            html.Div(
                                html.Span('Seleccionar KPI', style={'color': '#8f8f8f'}),
                            ),
                            dcc.Dropdown(
                                id='kpi-dropdown',
                            ),
                        ],
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                html.Span('Seleccionar Niveles', style={'color': '#8f8f8f'}),
                            ),
                            dcc.Dropdown(
                                id='niveles-dropdown',
                            ),
                        ],
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                html.Span('Seleccionar Tipos', style={'color': '#8f8f8f'}),
                            ),
                            dcc.Dropdown(
                                id='tipos-dropdown',
                                multi=True,
                            ),
                        ],
                    ),
                ],
                style={'marginBottom': '1%'}
            ),
            dbc.Row(  # Cuarta fila: Gráfico de líneas
                dbc.Col(
                    dcc.Graph(
                        id='line-graph',
                    ),
                ),
                style={'paddingBottom': '2%'}
            ),
        ],
        id='lineatiempo-main-container',
        style={'backgroundColor': '#f2f2f2'}
    )