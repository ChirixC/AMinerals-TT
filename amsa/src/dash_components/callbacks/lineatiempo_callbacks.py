from dash import Input, Output, State
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

from ...data_processing.data_loader import load_and_process_data
from ...config import DATA_AUTOGESTION_FILE_PATH

def register_lineatiempo_callbacks(app):
    """
    Registra los callbacks para la aplicación Dash que gestionan la actualización
    de los dropdowns y del gráfico basado en las interacciones del usuario.

    Los callbacks incluyen:
    - `populate_dropdowns`: Llena los dropdowns y el rango de fechas iniciales.
    - `actualizar_linea_graph`: Actualiza el gráfico de líneas según los filtros seleccionados.
    
    Args:
        app (dash.Dash): La instancia de la aplicación Dash.
    """
    
    @app.callback(
        [Output('lineas-date-picker', 'min_date_allowed'),
         Output('lineas-date-picker', 'max_date_allowed'),
         Output('lineas-date-picker', 'start_date'),
         Output('lineas-date-picker', 'end_date'),
         Output('kpi-dropdown', 'options'),
         Output('niveles-dropdown', 'options'),
         Output('tipos-dropdown', 'options')],
        [Input('lineatiempo-main-container', 'children')]
    )
    def populate_dropdowns(_):
        """
        Callback que llena los dropdowns de KPI, nivel y tipo, y establece el rango
        de fechas mínimo y máximo basado en los datos cargados.

        Returns:
            tuple: Un tuple con los valores para los dropdowns y las fechas mínimas y máximas.
        """
        
        # Cargar y procesar los datos desde la fuente
        df = load_and_process_data(source='local', filepath=DATA_AUTOGESTION_FILE_PATH)
        
        if df is None:
            return {}, {}, {}, {}, [], [], []
        
        # Preparar las opciones para los dropdowns
        kpi_options = [{'label': kpi, 'value': kpi} for kpi in df['id_kpi'].unique() if pd.notnull(kpi)]
        nivel_options = [{'label': nivel, 'value': nivel} for nivel in df['nivel'].unique() if pd.notnull(nivel)]
        tipo_options = [{'label': tipo, 'value': tipo} for tipo in df['tipo_dato'].unique() if pd.notnull(tipo)]
        
        # Obtener las fechas mínima y máxima
        min_date = df['fecha'].min()
        max_date = df['fecha'].max()
        
        # Convertir fechas a formato datetime
        min_date_format = datetime.strptime(min_date, '%m/%d/%Y %H:%M')
        max_date_format = datetime.strptime(max_date, '%m/%d/%Y %H:%M')
        
        return min_date_format, max_date_format, min_date_format, max_date_format, kpi_options, nivel_options, tipo_options
    
    @app.callback(
        Output('line-graph', 'figure'),
        [Input('lineas-date-picker', 'start_date'),
         Input('lineas-date-picker', 'end_date'),
         Input('kpi-dropdown', 'value'),
         Input('niveles-dropdown', 'value'),
         Input('tipos-dropdown', 'value')]
    )
    def actualizar_linea_graph(start_date, end_date, selected_kpi, selected_nivel, selected_tipo):
        """
        Callback que actualiza el gráfico de líneas basado en los filtros seleccionados.

        Args:
            start_date (str): La fecha de inicio seleccionada.
            end_date (str): La fecha de fin seleccionada.
            selected_kpi (str): El KPI seleccionado.
            selected_nivel (str): El nivel seleccionado.
            selected_tipo (list): La lista de tipos seleccionados.

        Returns:
            plotly.graph_objects.Figure: El gráfico de líneas actualizado.
        """
        
        if start_date is None or selected_kpi is None or end_date is None:
            fig = go.Figure()
            fig.update_layout(
                title='Gráfico de Línea',
                template='plotly_dark',
                xaxis_title='Fecha',
                yaxis_title='Valor',
                yaxis_tickformat='.2f'
            )
            return fig
        
        # Cargar y procesar los datos desde la fuente
        df = load_and_process_data(source='local', filepath=DATA_AUTOGESTION_FILE_PATH)
        if df is None:
            return go.Figure()
        
        # Convertir la columna 'fecha' a datetime
        df['fecha'] = pd.to_datetime(df['fecha'])
        
        # Filtrar los datos según el rango de fechas
        mask = (df['fecha'] >= start_date) & (df['fecha'] <= end_date)
        df_filtered = df.iloc[mask.values]
        
        # Filtrar por KPI, Nivel y Tipo
        if selected_kpi:
            df_filtered = df_filtered[df_filtered['id_kpi'] == selected_kpi]
        if selected_nivel:
            df_filtered = df_filtered[df_filtered['nivel'] == selected_nivel]
        if selected_tipo:
            df_filtered = df_filtered[df_filtered['tipo_dato'].isin(selected_tipo)]
        
        # Ordenar los datos por fecha y redondear los valores
        df_filtered = df_filtered.sort_values(by='fecha', ascending=True)
        df_filtered['valor'] = df_filtered['valor'].astype(float).round(2)
        
        # Obtener la unidad del dato
        unidad = df_filtered['unidad'].dropna().unique()
        unidad_str = f' ({unidad[0]})' if len(unidad) > 0 else ''
        
        # Crear el gráfico de líneas
        fig = px.line(df_filtered, x='fecha', y='valor', color='tipo_dato', title='Gráfico de Línea', template='plotly_dark')

        # Actualizar el diseño del gráfico
        fig.update_layout(
            xaxis_title='Fecha',
            yaxis_title=f'Valor{unidad_str}',
            yaxis_tickformat='.2f',
            legend_title='Tipo',
            template='plotly_dark'
        )
        
        return fig
