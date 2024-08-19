from dash import html, dcc
import dash_bootstrap_components as dbc
from .sidebar_layout import sidebar_layout
from .home_layout import home_layout
from dash import Input, Output, State

def app_layout():
    return dbc.Container(
        [    
            dcc.Location(id='url', refresh=False),
            dbc.Row(
                [
                    # Columna de la barra lateral
                    dbc.Col(
                        [
                            # Botón para colapsar o expandir la barra lateral
                            dbc.Button("☰", id="btn-sidebar", outline=True, color="primary", className="mb-3"),
                            # Componente colapsable que contiene la barra lateral
                            dbc.Collapse(sidebar_layout(), id="sidebar-collapse", is_open=True),
                        ],
                        xs=12, md=3, lg=2, style={"padding": "0"}  # Configuración de tamaño según la pantalla
                    ),
                    # Columna de contenido principal
                    dbc.Col(
                        # Div donde se renderizará el contenido de la página
                        html.Div(id='page-content'), 
                        xs=12, md=9, lg=10, style={"padding": "0"}
                    )
                ],
                style={"display": "flex"}
            )
        ],
        fluid=True,  # Contenedor fluido que ocupa todo el ancho de la pantalla
    )