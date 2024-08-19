import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient
from ..utils.data_config import get_data_source, get_azure_credentials
import io

def load_csv_data(filepath):
    """
    Carga datos desde un archivo CSV local.

    Parameters:
        filepath (str): La ruta al archivo CSV.

    Returns:
        DataFrame or None: Un DataFrame de pandas si la carga es exitosa, de lo contrario None.
    """
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

def load_azure_datalake_data(file_system_name, file_path):
    """
    Carga datos desde un archivo almacenado en Azure Data Lake.

    Parameters:
        file_system_name (str): El nombre del sistema de archivos en Azure Data Lake.
        file_path (str): La ruta al archivo dentro del sistema de archivos en Azure Data Lake.

    Returns:
        DataFrame or None: Un DataFrame de pandas si la carga es exitosa, de lo contrario None.
    """
    try:
        # Conectar al servicio Azure Data Lake utilizando las credenciales obtenidas
        credentials = get_azure_credentials()
        service_client = DataLakeServiceClient(
            account_url=f"https://{credentials['account_name']}.dfs.core.windows.net",
            credential=credentials['account_key']
        )
        
        # Obtener el cliente del sistema de archivos
        file_system_client = service_client.get_file_system_client(file_system=file_system_name)
        
        # Descargar el archivo desde Azure Data Lake
        file_client = file_system_client.get_file_client(file_path)
        download = file_client.download_file()
        downloaded_bytes = download.readall()
        
        # Convertir los bytes descargados en un DataFrame de pandas
        data = pd.read_csv(io.BytesIO(downloaded_bytes))
        return data
    
    except Exception as e:
        print(f"Error al cargar datos desde Azure Data Lake: {e}")
        return None

def load_and_process_data(source='local', filepath=None, file_system_name=None, file_path=None):
    """
    Carga y procesa datos desde una fuente especificada.

    Parameters:
        source (str): 'local' para archivos CSV, 'azure' para Azure Data Lake.
        filepath (str, optional): Ruta del archivo CSV (si source es 'local').
        file_system_name (str, optional): Nombre del sistema de archivos en Azure Data Lake (si source es 'azure').
        file_path (str, optional): Ruta del archivo dentro del sistema de archivos en Azure Data Lake (si source es 'azure').

    Returns:
        DataFrame or None: Un DataFrame con los datos procesados y limpios, o None si ocurre un error.
    """
    # Carga los datos desde la fuente especificada
    if source == 'local' and filepath:
        data = load_csv_data(filepath)
    elif source == 'azure' and file_system_name and file_path:
        data = load_azure_datalake_data(file_system_name, file_path)
    else:
        raise ValueError("Fuente de datos no especificada o parámetros insuficientes.")
    
    # Si los datos se cargaron con éxito, se procede a limpiarlos
    if data is not None:
        # Importar y aplicar la función de limpieza de datos
        from src.data_processing.data_cleaning import clean_data
        cleaned_data = clean_data(data)
        return cleaned_data
    
    return None
