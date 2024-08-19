from dash import html, dcc
import dash_bootstrap_components as dbc

def resumen_layout():
    """
    Crea y devuelve el diseño del resumen utilizando componentes de Dash y Dash Bootstrap Components.

    El diseño se compone de una serie de filas y columnas organizadas en un contenedor. 
    Cada columna contiene gráficos y comentarios, así como imágenes adicionales para la 
    representación visual de datos. Los gráficos están diseñados para mostrar información 
    sobre diferentes procesos, con líneas y puntos superpuestos para resaltar datos específicos.

    Returns:
        dbc.Container: Un contenedor que incluye todas las filas y columnas necesarias para 
                        el diseño de resumen.
    """
    return dbc.Container(
        [
            # Primera fila: Título del resumen
            dbc.Row([
                html.Div(
                    children=[
                        html.Span("PROCESO INTEGRADO | ", style={'fontWeight': 'bold', 'color': '#007993'}),
                        html.Span("Cumplimiento del 09 de Agosto al 15 de Agosto del 2024", style={'fontWeight': 'normal', 'color': '#007993'})
                    ],
                    style={'font-size': '16px', 'fontWeight': 'bold', 'display': 'inline-block', 'textAlign': 'center', 'width': '100%'}
                )
            ], align="center"),
             
            # Segunda fila: Gráficos de "Mina Col" y "Concentradora Col"
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.Div("Mina Col", className='text-center', id='mina-comments', 
                                        style={'position': 'absolute', 'zIndex': '1000', 'left': '5%'}),
                                
                                dcc.Graph(id='mina-graph',
                                          style={'height': '40vh', 'width': '70%', 'marginTop': '10%'}),
                                
                                html.Img(src='/assets/img/Vertical_Line.png', id='appearing-mina-vertical', 
                                         style={'width': '0.20%', 'height': '55%', 'position': 'absolute', 'left': '32.3%', 'top': '52%'}),
                               
                                html.Img(src='/assets/img/Horizontal_Line.png', id='appearing-mina-horizontal', 
                                         style={'width': '8%', 'height': '1%', 'position': 'absolute', 'left': '24.3%', 'top': '52%'}),
                                
                                html.Img(src='/assets/img/Dot_Circle.png', id='appearing-mina-dot', 
                                         style={'width': '1%', 'height': '4%', 'position': 'absolute', 'left': '23.5%', 'top': '51%'}),
                            ]
                        ),
                        width=6
                    ),
                    
                    dbc.Col(
                        html.Div(
                            [
                                html.Div("Concentradora Col", className='text-center', id='concentradora-comments',
                                         style={'position': 'absolute', 'zIndex': '1000', 'left': '57%'}),
                                
                                dcc.Graph(id='concentradora-graph',
                                          style={'height': '40vh', 'width': '70%', 'marginTop': '2%', 'marginLeft': '4%'}),
                                
                                html.Img(src='/assets/img/Vertical_Line.png', id='appearing-concentradora-vertical', 
                                         style={'width': '0.20%', 'height': '55%', 'position': 'absolute', 'left': '45.8%', 'top': '52%'}),
                               
                                html.Img(src='/assets/img/Horizontal_Line.png', id='appearing-concentradora-horizontal', 
                                         style={'width': '8%', 'height': '1%', 'position': 'absolute', 'left': '45.8%', 'top': '52%'}),
                                
                                html.Img(src='/assets/img/Dot_Circle.png', id='appearing-concentradora-dot', 
                                         style={'width': '1%', 'height': '4%', 'position': 'absolute', 'left': '53.3%', 'top': '51%'}),
                            ]
                        ),
                        width=6
                    ),
                ],
                style={'height': '33vh', 'position': 'relative'}
            ),
            
            # Tercera fila: Iconos y gráfico de "Productos"
            dbc.Row(
                [
                    dbc.Col(html.Div(className="text-center"), width=2),
                    
                    dbc.Col(
                        html.Div(
                            [
                                html.Img(src='/assets/img/Truck_Icon.png', id='flipping-image-1', style={'width': '20%', 'height': 'auto', 'marginRight': '-8%', 'marginTop': '-11%', 'zIndex': '1001'}),
                                html.Img(src='/assets/img/Chancado_Correas_Icon.png', id='flipping-image-2', style={'width': '20%', 'height': 'auto', 'marginRight': '-8%', 'marginTop': '11%', 'zIndex': '1001'}),
                                html.Img(src='/assets/img/Concentradora_Icon.png', id='flipping-image-3', style={'width': '20%', 'height': 'auto', 'marginRight': '-8%', 'marginTop': '-11%', 'zIndex': '1001'}),
                                html.Img(src='/assets/img/Pipe_Icon.png', id='flipping-image-4', style={'width': '20%', 'height': 'auto', 'marginRight': '-8%', 'marginTop': '11%', 'zIndex': '1001'}),
                                html.Img(src='/assets/img/Ship_Icon.png', id='flipping-image-5', style={'width': '20%', 'height': 'auto', 'marginTop': '-11%', 'zIndex': '1000'}),
                            ],
                            style={
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center',
                                    'height': '100%',
                                    'zIndex': '1000'
                                },
                            id='image-container'
                        ),
                        width=7,
                        style={'height': '33vh', 'position': 'relative'}
                    ),
                    
                    dbc.Col(
                        html.Div(
                            [
                                html.Div(className='text-center', id='productos-comments', 
                                         style={'position': 'absolute', 'zIndex': '100', 'left': '66%'}),
                                
                                dcc.Graph(id='productos-graph',
                                          style={'height': '40vh', 'width': '130%', 'zIndex': '99', 'marginTop': '20%', 'marginLeft': '-60%'}),
                                
                                html.Img(src='/assets/img/Horizontal_Line.png', id='appearing-productos-horizontal', 
                                         style={'width': '4%', 'height': '1%', 'position': 'absolute', 'left': '61.3%', 'top': '52%'}),
                                
                                html.Img(src='/assets/img/Dot_Circle.png', id='appearing-productos-dot', 
                                         style={'width': '1%', 'height': '4%', 'position': 'absolute', 'left': '64.6%', 'top': '51%'}),
                            ]
                        ),
                        width=3
                    ),
                ],
                style={'height': '33vh', 'position': 'relative'}
            ),
            
            # Cuarta fila: Gráficos de "Chancado" y "TFT"
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.Div(className='text-center', id='chancado-comments', 
                                         style={'position': 'absolute', 'zIndex': '1000', 'left': '5%'}),
                                
                                dcc.Graph(id='chancado-graph',
                                          style={'height': '40vh', 'width': '70%', 'marginTop': '-5%'}),
                                
                                html.Img(src='/assets/img/Vertical_Line.png', id='appearing-chancado-vertical', 
                                         style={'width': '0.20%', 'height': '65%', 'position': 'absolute', 'zIndex': '1000', 'left': '35%', 'top': '-26%'}),
                               
                                html.Img(src='/assets/img/Horizontal_Line.png', id='appearing-chancado-horizontal', 
                                         style={'width': '8%', 'height': '1%', 'position': 'absolute', 'zIndex': '1000', 'left': '27%', 'top': '38%'}),
                                
                                html.Img(src='/assets/img/Dot_Circle.png', id='appearing-chancado-dot', 
                                         style={'width': '1%', 'height': '4%', 'position': 'absolute', 'zIndex': '1000', 'left': '26.4%', 'top': '36.6%'}),
                            ]
                        ),
                        width=6
                    ),
                    
                    dbc.Col(
                        html.Div(
                            [
                                html.Div(className='text-center', id='tft-comments', 
                                         style={'position': 'absolute', 'zIndex': '1000', 'left': '40%'}),
                                
                                dcc.Graph(id='tft-graph',
                                          style={'height': '40vh', 'width': '70%', 'marginTop': '-3%', 'marginLeft': '-35%'}),
                                
                                html.Img(src='/assets/img/Vertical_Line.png', id='appearing-tft-vertical', 
                                         style={'width': '0.20%', 'height': '20%', 'position': 'absolute', 'left': '47.8%', 'top': '-30%'}),
                                
                                html.Img(src='/assets/img/Dot_Circle.png', id='appearing-tft-dot', 
                                         style={'width': '1%', 'height': '4%', 'position': 'absolute', 'left': '47.4%', 'top': '-11%'}),
                            ]
                        ),
                        width=6
                    ),
                ],
                style={'height': '33vh', 'position': 'relative', 'padding': '0'}
            )
        ]
    )
