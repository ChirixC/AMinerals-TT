from dash import html, dcc
import dash_bootstrap_components as dbc
from ..styles.sidebar_style import sidebar_styles

# Cargar los estilos personalizados para la barra lateral
styles = sidebar_styles()

def sidebar_layout():
    """
    Crea y devuelve el diseño de la barra lateral utilizando componentes de Dash y Dash Bootstrap Components.

    El diseño de la barra lateral incluye un título, una línea horizontal y una navegación vertical con enlaces.
    La barra lateral está diseñada para ser visible en pantallas medianas y grandes, y oculta en pantallas pequeñas.

    Returns:
        dbc.Col: Un componente de columna que contiene el diseño de la barra lateral.
    """
    return dbc.Col(
        [

            
            # Encabezado de la barra lateral
            html.H3("Menu", className="display-4"),
            
            # Línea horizontal para separación
            html.Hr(),
            
            # Navegación vertical con enlaces
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Resumen", href="/resumen", active="exact"),
                    dbc.NavLink("Linea Tiempo", href="/lineatiempo", active="exact"),
                ],
                vertical=True,
                pills=True,
                className="flex-column"
            ),
        ],
        id="sidebar",
        style=styles['main-sidebar'],  # Aplicar estilos personalizados
        className="d-none d-md-block"  # Ocultar en pantallas xs/sm, mostrar en md y más
    )
