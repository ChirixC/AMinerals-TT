from dash import Input, Output, State
import dash_bootstrap_components as dbc
from dash import dcc, html

def register_sidebar_callbacks(app):
    """
    Registra los callbacks para la barra lateral en la aplicación Dash.

    El callback vinculado a este método controla la apertura y el cierre
    de la barra lateral cuando se hace clic en el botón correspondiente.

    Args:
        app (Dash): La instancia de la aplicación Dash a la que se le registrarán los callbacks.
    """
    
    @app.callback(
        Output("sidebar-collapse", "is_open"),
        Input("btn-sidebar", "n_clicks"),
        State("sidebar-collapse", "is_open"),
    )
    def toggle_sidebar(n_clicks, is_open):
        """
        Alterna el estado de la barra lateral entre abierto y cerrado.

        Este callback se activa cuando se hace clic en el botón de la barra lateral.
        
        Args:
            n_clicks (int): El número de veces que se ha hecho clic en el botón de la barra lateral.
            is_open (bool): El estado actual de la barra lateral (abierto o cerrado).
        
        Returns:
            bool: El nuevo estado de la barra lateral (abierto si estaba cerrado y viceversa).
        """
        if n_clicks:
            return not is_open
        return is_open

    # TODO: Mejorar responsividad
    # Considerar ajustar el diseño de la barra lateral para que se adapte mejor a diferentes tamaños de pantalla
    # y dispositivos móviles. Investigar sobre técnicas de diseño responsivo y aplicarlas aquí.