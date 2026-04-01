import streamlit as st
import pandas as pd
import time
import os

st.set_page_config(page_title="Visor de Promodescuentos - Pantalla Automática", layout="wide")

@st.cache_data
def load_data(path):
    if not os.path.exists(path):
        return pd.DataFrame()
    ds = pd.read_csv(path)
    required_columns = ['img src', 'button href (2)', 'text--b']
    # Ensure columns exist
    for col in required_columns:
        if col not in ds.columns:
            ds[col] = None
    return ds[required_columns].copy()

# Cargar los datos
file_path = "data.csv"
ds = load_data(file_path)

if ds.empty:
    st.error("No se encontró el archivo 'data.csv' o está vacío. Por favor, asegúrate de que exista.")
    st.stop()

# Configuración del Sidebar
st.sidebar.title("Configuración de Visualización")
modo_automatico = st.sidebar.toggle("Activar Modo Pantalla Automática")
velocidad = st.sidebar.slider("Velocidad de transición (segundos)", min_value=2, max_value=10, value=3)

st.title("Visor de Ofertas - Promodescuentos")

if not modo_automatico:
    st.markdown("### Vista de Catálogo Completo")
    st.markdown("Modo interactivo con imágenes y enlaces. Activa el Modo Automático en la barra lateral.")

    # Preparar datos para la tabla
    df_display = ds.copy()
    df_display.rename(columns={
        'img src': 'Imagen',
        'button href (2)': 'Enlace',
        'text--b': 'Descripción'
    }, inplace=True)

    st.dataframe(
        df_display,
        column_config={
            "Imagen": st.column_config.ImageColumn("Imagen de la oferta", help="Previsualización"),
            "Enlace": st.column_config.LinkColumn("Enlace a la oferta", display_text="Ir a la oferta 🔗"),
            "Descripción": st.column_config.TextColumn("Descripción / Título", width="large")
        },
        hide_index=True,
        use_container_width=True,
        height=600
    )

else:
    st.markdown("### Modo Presentación Automática 📺")
    st.markdown(f"Rotando ofertas cada **{velocidad} segundos**...")

    # Espacio reservado para las tarjetas de producto
    placeholder = st.empty()

    # Bucle infinito para rotar ofertas
    while True:
        for idx, row in ds.iterrows():
            img_url = row['img src']
            enlace = row['button href (2)']
            descripcion = row['text--b']

            # Manejo de nulos (NaN)
            img_url = img_url if pd.notna(img_url) else "https://via.placeholder.com/300x300?text=Sin+Imagen"
            enlace = enlace if pd.notna(enlace) else "#"
            descripcion = descripcion if pd.notna(descripcion) else "Oferta sin descripción"

            with placeholder.container():
                # Diseño de la tarjeta centrada
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.markdown(
                        f"""
                        <div style="text-align: center; padding: 20px; border-radius: 15px; background-color: #f0f2f6; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                            <img src="{img_url}" style="max-width: 100%; max-height: 400px; border-radius: 10px; object-fit: contain;">
                            <h2 style="color: #1f77b4; margin-top: 20px;">{descripcion}</h2>
                            <a href="{enlace}" target="_blank" style="display: inline-block; background-color: #ff6a00; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 18px; margin-top: 15px;">
                                ¡Ver Oferta! 🛒
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            # Pausa según el slider
            time.sleep(velocidad)
