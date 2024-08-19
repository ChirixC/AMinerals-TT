import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
DATA_GRAFICOS_FILE_PATH = os.getenv('DATA_GRAFICOS_FILE_PATH')
DATA_COMMENTS_FILE_PATH = os.getenv('DATA_COMMENTS_FILE_PATH')