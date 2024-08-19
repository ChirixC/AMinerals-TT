from dash import Dash, html
import dash_bootstrap_components as dbc
from src.dash_components.layouts.app_layout import app_layout
from src.dash_components.callbacks.register_callbacks import register_callbacks
from src.dash_components.callbacks.home_callbacks import register_home_callbacks
import os


def init_app():
    """
    Inicializa y configura la aplicación Dash.
    
    Crea una instancia de la aplicación Dash, define el layout y registra los callbacks necesarios.
    Luego, inicia el servidor de la aplicación en modo debug.

    Returns:
        None
    """
    # Inicialización de la aplicación Dash
    app = Dash(
        __name__,
        suppress_callback_exceptions=True,
        pages_folder=os.path.join(os.getcwd(), 'src\\dash_components\\layouts'),
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )
    
    # Configuración de layouts y registro de callbacks
    app.layout = app_layout
    register_callbacks(app)

    # Inicia el servidor de la aplicación
    app.run_server(debug=True)
    

if __name__ == '__main__':
    # Punto de entrada principal de la aplicación
    init_app()