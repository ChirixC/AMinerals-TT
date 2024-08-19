import os

def get_azure_credentials():
    """Obtiene las credenciales para Azure Data Lake desde las variables de entorno.

    Retorna un diccionario con el nombre de cuenta y la clave de cuenta de Azure.
    Si las variables de entorno no están definidas, se usan valores predeterminados.
    
    Returns:
        dict: Un diccionario con las claves 'account_name' y 'account_key'.
    """
    return {
        'account_name': os.getenv('AZURE_ACCOUNT_NAME', 'default_account_name'),
        'account_key': os.getenv('AZURE_ACCOUNT_KEY', 'default_account_key'),
    }

def get_data_source():
    """
    Determina la fuente de datos predeterminada.

    Esta función obtiene el valor de la variable de entorno 'DATA_SOURCE'.
    Si no está definida, retorna 'local' como valor predeterminado.
    
    Returns:
        str: La fuente de datos ('local' o 'azure').
    """
    return os.getenv('DATA_SOURCE', 'local')