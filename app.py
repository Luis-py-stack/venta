import streamlit as st
import pandas as pd

st.set_page_config(page_title="Visor de Promodescuentos", layout="wide")

st.title("Visor de Ofertas - Promodescuentos")
st.markdown("Sube tu archivo CSV para visualizar las ofertas con imágenes y enlaces interactivos.")

# Componente para subir el archivo
uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None:
    try:
        # Leemos el CSV
        ds = pd.read_csv(uploaded_file)

        # Verificamos que existan las columnas requeridas
        required_columns = ['img src', 'button href (2)', 'text--b']
        missing_columns = [col for col in required_columns if col not in ds.columns]

        if missing_columns:
            st.error(f"El archivo CSV no tiene las columnas necesarias: {', '.join(missing_columns)}")
        else:
            # Tomamos las primeras 50 filas y seleccionamos solo las columnas que nos interesan
            df_display = ds[required_columns].head(50).copy()

            # Renombramos las columnas para que sean más amigables en la tabla
            df_display.rename(columns={
                'img src': 'Imagen',
                'button href (2)': 'Enlace',
                'text--b': 'Descripción'
            }, inplace=True)

            st.subheader("Top 50 Ofertas")

            # Mostramos el dataframe usando st.dataframe y st.column_config
            st.dataframe(
                df_display,
                column_config={
                    "Imagen": st.column_config.ImageColumn(
                        "Imagen de la oferta",
                        help="Previsualización de la oferta"
                    ),
                    "Enlace": st.column_config.LinkColumn(
                        "Enlace a la oferta",
                        display_text="Ir a la oferta 🔗"
                    ),
                    "Descripción": st.column_config.TextColumn(
                        "Descripción / Título",
                        width="large"
                    )
                },
                hide_index=True,
                use_container_width=True,
                height=600
            )

    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
else:
    st.info("Esperando a que subas un archivo CSV.")
