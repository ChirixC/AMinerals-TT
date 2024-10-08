@echo off

:: Crear un entorno virtual
python -m venv .venv

:: Activar el entorno virtual
call .venv\Scripts\activate

:: Instalar dependencias
-m pip install --upgrade pip
pip install -r requirements.txt

:: Ejecutar la aplicación
start /B python main.py

:: Esperar un momento para asegurarse de que la aplicación se haya iniciado
timeout /t 5 /nobreak >nul

:: Abrir la URL en el navegador predeterminado
start http://127.0.0.1:8050/

:: Obtener la URL de la aplicación
echo La aplicación debería estar corriendo en http://127.0.0.1:8050/
