from dash import html, dcc
import dash_bootstrap_components as dbc
from ..styles.home_styles import home_styles

styles = home_styles()

def home_layout():
    """
    Define el diseño para la página de inicio de la aplicación.

    Returns:
        dbc.Container: Contenedor principal que incluye el título, la información personal,
                        el botón y el área de salida del contador.
    """
    return dbc.Container(
        [
            # Fila para el título principal
            dbc.Row(
                dbc.Col(
                    html.H1("Home Page", style=styles["header"]),
                    width={"size": 6, "offset": 3}
                ),
                className="mb-4"
            ),
            # Fila para la información personal y el botón
            dbc.Row(
                dbc.Col([
                    # Información personal
                    html.Span("César Chirino", style={'font-size': '24px', 'fontWeight': 'bold', 'display': 'block'}),
                    html.Span("Data Scientist", style={'font-size': '20px', 'display': 'block'}),
                    html.Span("Bienvenidos a mi solución a la prueba técnica para AMinerals 2024", style={'font-size': '16px', 'display': 'block'}),
                    html.Span("Espero sea de su agrado", style={'font-size': '16px', 'display': 'block'}),
                    
                    # Espaciado adicional
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    
                    # Botón para incrementar el contador
                    html.Button('No me toques', id='increment-button', n_clicks=0, style={'marginTop': '10px'}),
                    
                    # Área para mostrar el resultado del contador
                    html.Div(id='counter-output', style={'marginTop': '20px', 'font-size': '18px'}),
                ], width={"size": 6, "offset": 3}),
                className="mb-4"
            )
        ],
        fluid=True,  # Utiliza un contenedor fluido que se ajusta al ancho de la pantalla
        style=styles["main"]  # Aplica estilos definidos en home_styles
    )
