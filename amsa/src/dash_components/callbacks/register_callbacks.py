from dash import Dash, Input, Output
from .home_callbacks import register_home_callbacks
from .resumen_callbacks import register_resumen_callbacks
from .lineatiempo_callbacks import register_lineatiempo_callbacks
from .sidebar_callback import register_sidebar_callbacks

from ..layouts.home_layout import home_layout
from ..layouts.resumen_layout import resumen_layout
from ..layouts.lineatiempo_layout import lineatiempo_layout

def register_callbacks(app: Dash):
    """
    Registra todos los callbacks necesarios para la aplicación Dash.
    
    Parameters:
        app (Dash): La instancia de la aplicación Dash.
    
    TODO: Minimizar código de reivisión / registro de callbacks
    """
    
    # Verifica si los callbacks de la barra lateral ya han sido registrados
    if not hasattr(app, 'callbacks_registered_sidebar'):
        register_sidebar_callbacks(app)
        app.callbacks_registered_sidebar = True
    # Verifica si los callbacks de la página de inicio ya han sido registrados
    if not hasattr(app, 'callbacks_registered_home'):
        register_home_callbacks(app)
        app.callbacks_registered_home = True
    
    # Verifica si los callbacks de la página de resumen ya han sido registrados
    if not hasattr(app, 'callbacks_registered_resumen'):
        register_resumen_callbacks(app)
        app.callbacks_registered_resumen = True
    
    # Verifica si los callbacks de la página de Linea tiempo ya han sido registrados
    if not hasattr(app, 'callbacks_registered_lineatiempo'):
        register_lineatiempo_callbacks(app)
        app.callbacks_registered_lineatiempo = True
    
    
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
        elif pathname == '/lineatiempo':
            return lineatiempo_layout()
        else:
            return "404 Page Not Found"
