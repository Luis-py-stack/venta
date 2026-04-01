# Visor de Promodescuentos en Streamlit

Este proyecto es una aplicación web interactiva desarrollada con [Streamlit](https://streamlit.io/) para visualizar ofertas exportadas de Promodescuentos mediante un archivo CSV.

## Características

- Carga automática de `data.csv` en el servidor con `@st.cache_data`.
- **Vista Normal**: Visualización de catálogo completo en una tabla interactiva con imágenes y enlaces.
- **Modo Presentación Automática**: Rotación automática de tarjetas de productos, ideal para pantallas de publicidad, con velocidad configurable.
- Interfaz atractiva y profesional con manejo de datos faltantes.

## Cómo ejecutar localmente

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener el archivo `data.csv` en la misma carpeta que `app.py`.
3. Abre tu terminal e instala las dependencias (se recomienda usar un entorno virtual):
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación de Streamlit:
   ```bash
   streamlit run app.py
   ```
5. Usa la barra lateral para alternar entre la vista normal y el modo de presentación automática.

## Formato del archivo CSV requerido (`data.csv`)

El archivo debe llamarse `data.csv` y contar con al menos las siguientes columnas:
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