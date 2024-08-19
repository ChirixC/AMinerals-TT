from dash import Input, Output, State
from dash.exceptions import PreventUpdate

def register_home_callbacks(app):
    """
    Registra los callbacks para la página de inicio de la aplicación Dash.

    Parameters:
        app (Dash): La instancia de la aplicación Dash.
    """
    print('entra en register_home_callback')

    @app.callback(
        Output('counter-output', 'children'),
        Input('increment-button', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_counter(n_clicks):
        """
        Actualiza el contador y genera un mensaje basado en el número de clics.

        Parameters:
            n_clicks (int): El número de veces que se ha hecho clic en el botón.

        Returns:
            str: Un mensaje que incluye el número de clics y un mensaje especial si el número coincide con ciertos valores.
        """
        # Si no se ha hecho clic, se evita la actualización
        if n_clicks is None:
            raise PreventUpdate

        # Inicializar el mensaje vacío
        message = ""

        # Condicionales para generar mensajes específicos según el número de clics
        if n_clicks == 1:
            message = "Explotó la app"
        elif n_clicks == 3:
            message = "Esto es una prueba de callback"
        elif n_clicks == 7:
            message = "No tenía pensado borrarla"
        elif n_clicks == 15:
            message = "Deberías ver el resto de la app"
        elif n_clicks == 1000000:
            message = "Seguro lo viste en el código. Trampa"   

        # Retorna el número de clics junto con el mensaje generado
        return f"{n_clicks}. {message}"
