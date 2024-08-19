from dash import html

def extraer_df_data(df):
    """
    Extrae los datos necesarios de un DataFrame para generar los comentarios de la sección.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de KPIs.

    Returns:
        tuple: Una tupla que contiene listas de KPIs, valores de PS, valores de PM, unidades, porcentajes calculados,
               el porcentaje máximo y el índice del KPI con el mayor porcentaje.
    """
    # Extraer datos de KPI, PS, PM y unidades
    kpis = df['kpi_visualizacion'].tolist()
    ps_values = df['ps'].round().tolist()
    pm_values = df['pm'].round().tolist()
    units = df['unidad'].tolist()
    
    # Calcular porcentajes de cada KPI
    percentages = [round((pm / ps) * 100) for ps, pm in zip(df['ps'], df['pm'])]

    # Encontrar el máximo porcentaje y su índice correspondiente
    max_index = max(range(len(percentages)), key=lambda i: percentages[i])
    max_percentage = percentages[max_index]   
    
    return kpis, ps_values, pm_values, units, percentages, max_percentage, max_index

def crear_comments(df, seccion):
    """
    Genera un bloque de comentarios en formato HTML para una sección específica de la página.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de la sección.
        seccion (str): El nombre de la sección para la cual se generan los comentarios.

    Returns:
        dash.html.Div: Un componente HTML de Dash que contiene los comentarios formateados.
    """
    # Filtrar el DataFrame para la sección específica
    df = df[df['seccion'] == seccion].copy()
    
    # Extraer datos relevantes del DataFrame
    kpis, ps_values, pm_values, units, percentages, max_percentage, max_index = extraer_df_data(df)
    
    details = []
    
    # Crear una lista de componentes HTML para cada KPI
    for i in range(len(kpis)):
        details.append(
            html.Span(f"· {kpis[i]}: {ps_values[i]}{units[i]} vs {pm_values[i]}{units[i]} ({percentages[i]}%)", style={'color': 'black'})
        )
        details.append(html.Br())  # Agregar salto de línea después de cada comentario de KPI

    return html.Div([
        html.Div([
            html.Span(f"{seccion}: ", style={'fontWeight': 'bold', 'color': '#007993'}),
            html.Span(f"{max_percentage}% {kpis[max_index]}", style={'fontWeight': 'bold', 'color': '#00df00'}),
        ], style={'fontSize': '16px', 'fontWeight': 'bold'}),
        
        # Detalles para cada KPI
        html.Div(details, style={'fontSize': '12px'}),

    ], style={'textAlign': 'left'})
