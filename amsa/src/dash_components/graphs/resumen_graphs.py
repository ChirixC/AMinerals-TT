import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def crear_grafico(df, seccion):
    """
    Crea un gráfico basado en los datos filtrados por sección y columnas especificadas.

    Parameters:
    - df (pandas.DataFrame): DataFrame con los datos a graficar.
    - seccion (str): Sección específica del DataFrame para la cual se creará el gráfico.

    Returns:
    - fig (plotly.graph_objects.Figure): Objeto gráfico de Plotly con el gráfico generado.
    """
    
    # Filtrar el DataFrame para la sección especificada
    df = df[df['seccion'] == seccion].copy()
    
    # Convertir la columna 'timestamp' a un formato de fecha y extraer el día y mes
    df.loc[:, 'Fecha'] = pd.to_datetime(df['timestamp'], format='%Y%m%d')

    # Obtener el KPI primario para el título de la gráfica
    kpi_primario = df['kpi_primario'].iloc[0]

    # Crear la figura utilizando go.Figure()
    fig = go.Figure()
    
    # Agregar una barra para 'valor_secundario'
    fig.add_trace(go.Bar(
        x=df['Fecha'],
        y=df['valor_secundario'],
        name=f"{kpi_primario} Real",
        textfont=dict(
            color='white',  # Color del texto dentro de las barras
            family='Arial, sans-serif',  # Familia de la fuente
            size=14,  # Tamaño del texto
            weight=600,
        ),
        marker_color='#bfbfbf',  # Color de las barras
        marker_line_width=1.5,  # Grosor del borde de las barras
    ))
    
    # Agregar una línea verde para 'valor_primario'
    fig.add_trace(go.Scatter(
        x=df['Fecha'],
        y=df['valor_primario'],
        mode='lines+markers',
        name=f"{kpi_primario} PS",
        line=dict(color='#00df00')
    ))
    
    # Actualizar el diseño del gráfico
    fig.update_layout(
        plot_bgcolor='white',
        showlegend=True,
        legend=dict(
            x=0.5,
            y=-0.15,
            orientation="h",
            traceorder="normal",
            font=dict(size=10),
            xanchor='center'
        ),
        xaxis_title='',  # Eliminar la etiqueta del eje X
        yaxis_title='',  # Eliminar la etiqueta del eje Y
        yaxis=dict(
            tickfont=dict(
                size=12,
                color='black'
            ),
        ),
        xaxis=dict(
            tickformat='%d-%m',  # Formato de fecha
        ),
    )
    
    # Agregar anotaciones de texto en la parte inferior de las barras
    for i, value in enumerate(df['valor_primario']):
        if value == 0:
            text_ = ''
            text_angle = 0
            y_ = 0
        elif value < 0.1:
            text_ = round(value, 2)
            text_angle = 0
            y_ = 0
        else:
            text_ = round(value, 2)
            text_angle = 270
            y_ = 0.1

        # Añadir anotaciones de texto al gráfico
        fig.add_annotation(
            x=df['Fecha'].iloc[i],
            y=y_,  # Ubicar el texto en la parte inferior de la barra
            text=f"{text_}",
            textangle=text_angle,
            showarrow=False,
            font=dict(
                size=14,
                color='white',
                family='Arial, sans-serif',
                weight='bold'
            ),
            align='center',
            xanchor='center',
            yanchor='bottom',
        )
        
    return fig
