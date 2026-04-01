# Visor de Promodescuentos en Streamlit

Este proyecto es una aplicación web interactiva desarrollada con [Streamlit](https://streamlit.io/) para visualizar ofertas exportadas de Promodescuentos mediante un archivo CSV.

## Características

- Carga interactiva de archivos CSV (`st.file_uploader`).
- Visualización de imágenes en la tabla.
- Enlaces de texto clickeables.
- Visualización de los top 50 resultados directamente en pantalla.

## Cómo ejecutar localmente

1. Clona este repositorio o descarga los archivos.
2. Abre tu terminal e instala las dependencias (se recomienda usar un entorno virtual):
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación de Streamlit:
   ```bash
   streamlit run app.py
   ```
4. Sube tu archivo CSV en la interfaz y visualiza los datos de las ofertas.

## Formato del archivo CSV requerido

El archivo subido deberá contar con al menos las siguientes columnas:
- `img src`
- `button href (2)`
- `text--b`

## Cómo realizar el despliegue (Deploy) en Streamlit Community Cloud

Para desplegar esta aplicación públicamente en Streamlit Community Cloud, sigue estos pasos:

1. Asegúrate de tener este código en un repositorio público o privado en tu cuenta de GitHub.
2. Ingresa a [Streamlit Community Cloud](https://share.streamlit.io/) y vincula tu cuenta de GitHub.
3. Haz clic en "New App" (Nueva App).
4. Selecciona tu repositorio, rama (`main` o `master`), y el nombre del archivo principal que en este caso es `app.py`.
5. Haz clic en "Deploy!"

Streamlit instalará automáticamente los paquetes especificados en el `requirements.txt` y desplegará la aplicación.