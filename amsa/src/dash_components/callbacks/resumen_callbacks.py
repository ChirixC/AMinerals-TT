from dash import Input, Output, State
from ..graphs.resumen_graphs import crear_grafico
from ..graphs.resumen_comments import crear_comments
from ...data_processing.data_loader import load_and_process_data
from ...config import DATA_GRAFICOS_FILE_PATH, DATA_COMMENTS_FILE_PATH

# TODO: El load data debería cargarla a caché sólo si cambió la data, habría que verificarla con un HASH
def register_resumen_callbacks(app):
    """
    Registra todos los callbacks relacionados con la página de resumen de la aplicación Dash.
    
    Parameters:
        app (Dash): La instancia de la aplicación Dash.
    """

    # ---------------------------
    # BLOQUE DE CALLBACKS: GRÁFICOS
    # ---------------------------

    @app.callback(
        Output('mina-graph', 'figure'),
        [Input('url', 'pathname')],
        [State('mina-graph', 'id')]
    )
    def actualizar_grafico(pathname, graph_id):
        """
        Callback para actualizar el gráfico de Mina en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
            graph_id (str): El ID del gráfico de Mina.
        
        Returns:
            dict: La figura (gráfico) generada para la sección Mina.
        """
        if pathname == '/resumen':
            data = load_and_process_data(source='local', filepath=DATA_GRAFICOS_FILE_PATH)
            return crear_grafico(data, "MINA")

    @app.callback(
        Output('concentradora-graph', 'figure'),
        [Input('url', 'pathname')],
        [State('concentradora-graph', 'id')]
    )
    def actualizar_grafico(pathname, graph_id):
        """
        Callback para actualizar el gráfico de Concentradora en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
            graph_id (str): El ID del gráfico de Concentradora.
        
        Returns:
            dict: La figura (gráfico) generada para la sección Concentradora.
        """
        if pathname == '/resumen':
            data = load_and_process_data(source='local', filepath=DATA_GRAFICOS_FILE_PATH)
            return crear_grafico(data, "CONCENTRADORA")

    @app.callback(
        Output('productos-graph', 'figure'),
        [Input('url', 'pathname')],
        [State('productos-graph', 'id')]
    )
    def actualizar_grafico(pathname, graph_id):
        """
        Callback para actualizar el gráfico de Productos en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
            graph_id (str): El ID del gráfico de Productos.
        
        Returns:
            dict: La figura (gráfico) generada para la sección Productos.
        """
        if pathname == '/resumen':
            data = load_and_process_data(source='local', filepath=DATA_GRAFICOS_FILE_PATH)
            return crear_grafico(data, "PRODUCTO")

    @app.callback(
        Output('chancado-graph', 'figure'),
        [Input('url', 'pathname')],
        [State('chancado-graph', 'id')]
    )
    def actualizar_grafico(pathname, graph_id):
        """
        Callback para actualizar el gráfico de Chancado y Correas en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
            graph_id (str): El ID del gráfico de Chancado y Correas.
        
        Returns:
            dict: La figura (gráfico) generada para la sección Chancado y Correas.
        """
        if pathname == '/resumen':
            data = load_and_process_data(source='local', filepath=DATA_GRAFICOS_FILE_PATH)
            return crear_grafico(data, "CHANCADO Y CORREAS")

    @app.callback(
        Output('tft-graph', 'figure'),
        [Input('url', 'pathname')],
        [State('tft-graph', 'id')]
    )
    def actualizar_grafico(pathname, graph_id):
        """
        Callback para actualizar el gráfico de TFT en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
            graph_id (str): El ID del gráfico de TFT.
        
        Returns:
            dict: La figura (gráfico) generada para la sección TFT.
        """
        if pathname == '/resumen':
            data = load_and_process_data(source='local', filepath=DATA_GRAFICOS_FILE_PATH)
            return crear_grafico(data, "TFT")

    # ---------------------------
    # BLOQUE DE CALLBACKS: COMENTARIOS
    # ---------------------------

    @app.callback(
        Output('mina-comments', 'children'),
        [Input('url', 'pathname')]
    )
    def actualizar_comments(pathname):
        """
        Callback para actualizar los comentarios de Mina en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
        
        Returns:
            list: Los comentarios generados para la sección Mina.
        """
        if pathname == '/resumen':
            data_comments = load_and_process_data(source='local', filepath=DATA_COMMENTS_FILE_PATH)
            return crear_comments(data_comments, "MINA")

    @app.callback(
        Output('concentradora-comments', 'children'),
        [Input('url', 'pathname')]
    )
    def actualizar_comments(pathname):
        """
        Callback para actualizar los comentarios de Concentradora en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
        
        Returns:
            list: Los comentarios generados para la sección Concentradora.
        """
        if pathname == '/resumen':
            data_comments = load_and_process_data(source='local', filepath=DATA_COMMENTS_FILE_PATH)
            return crear_comments(data_comments, "CONCENTRADORA")

    @app.callback(
        Output('productos-comments', 'children'),
        [Input('url', 'pathname')]
    )
    def actualizar_comments(pathname):
        """
        Callback para actualizar los comentarios de Productos en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
        
        Returns:
            list: Los comentarios generados para la sección Productos.
        """
        if pathname == '/resumen':
            data_comments = load_and_process_data(source='local', filepath=DATA_COMMENTS_FILE_PATH)
            return crear_comments(data_comments, "PRODUCTO")

    @app.callback(
        Output('chancado-comments', 'children'),
        [Input('url', 'pathname')]
    )
    def actualizar_comments(pathname):
        """
        Callback para actualizar los comentarios de Chancado y Correas en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
        
        Returns:
            list: Los comentarios generados para la sección Chancado y Correas.
        """
        if pathname == '/resumen':
            data_comments = load_and_process_data(source='local', filepath=DATA_COMMENTS_FILE_PATH)
            return crear_comments(data_comments, "CHANCADO Y CORREAS")

    @app.callback(
        Output('tft-comments', 'children'),
        [Input('url', 'pathname')]
    )
    def actualizar_comments(pathname):
        """
        Callback para actualizar los comentarios de TFT en la página de resumen.
        
        Parameters:
            pathname (str): La ruta actual en la barra de direcciones del navegador.
        
        Returns:
            list: Los comentarios generados para la sección TFT.
        """
        if pathname == '/resumen':
            data_comments = load_and_process_data(source='local', filepath=DATA_COMMENTS_FILE_PATH)
            return crear_comments(data_comments, "TFT")

    return {}
