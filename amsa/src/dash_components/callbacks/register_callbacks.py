from dash import Dash, Input, Output
from .home_callbacks import register_home_callbacks
from .resumen_callbacks import register_resumen_callbacks
from ..layouts.home_layout import home_layout
from ..layouts.resumen_layout import resumen_layout

def register_callbacks(app: Dash):
    """
    Registra todos los callbacks necesarios para la aplicación Dash.
    
    Parameters:
        app (Dash): La instancia de la aplicación Dash.
    """
    # Verifica si los callbacks de la página de inicio ya han sido registrados
    if not hasattr(app, 'callbacks_registered_home'):
        register_home_callbacks(app)
        app.callbacks_registered_home = True
    
    # Verifica si los callbacks de la página de resumen ya han sido registrados
    if not hasattr(app, 'callbacks_registered_resumen'):
        register_resumen_callbacks(app)
        app.callbacks_registered_resumen = True
    
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        """
        Callback para actualizar el contenido de la página según la URL actual.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
        
        Returns:
            html.Div: El layout correspondiente a la página actual o un mensaje de error 404.
        """
        print(pathname)
        print('entra en display')
        
        # Lógica de enrutamiento para devolver el layout correspondiente según la URL
        if pathname == '/':
            return home_layout()
        elif pathname == '/resumen':
            return resumen_layout()
        else:
            return "404 Page Not Found"
