import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Visor de Promodescuentos - Pantalla Automática", layout="wide")

@st.cache_data
def load_data(uploaded_file):
    ds = pd.read_csv(uploaded_file)
    required_columns = ['img src', 'button href (2)', 'text--b']

    # Check for price column (case insensitive)
    price_col = None
    for col in ds.columns:
        if 'precio' in col.lower() or 'price' in col.lower():
            price_col = col
            break

    # Ensure mandatory columns exist
    for col in required_columns:
        if col not in ds.columns:
            ds[col] = None

    if price_col:
        required_columns.append(price_col)
        # Rename price column internally for easy access
        ds.rename(columns={price_col: 'precio_final'}, inplace=True)
        required_columns[-1] = 'precio_final'
    else:
        # If no price column found, add a dummy one
        ds['precio_final'] = None
        required_columns.append('precio_final')

    return ds[required_columns].copy()

# Configuración del Sidebar
st.sidebar.title("Configuración de Visualización")
modo_automatico = st.sidebar.toggle("Activar Modo Pantalla Automática")
velocidad = st.sidebar.slider("Velocidad de transición (segundos)", min_value=2, max_value=10, value=3)

st.title("Visor de Ofertas - Promodescuentos")
st.markdown("Sube tu archivo CSV para visualizar las ofertas. Cambia al Modo Automático desde la barra lateral.")

uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None:
    try:
        ds = load_data(uploaded_file)

        if not modo_automatico:
            st.markdown("### Vista de Catálogo Completo")

            # Preparar datos para la tabla
            df_display = ds.copy()
            df_display.rename(columns={
                'img src': 'Imagen',
                'button href (2)': 'Enlace',
                'text--b': 'Descripción',
                'precio_final': 'Precio'
            }, inplace=True)

            st.dataframe(
                df_display,
                column_config={
                    "Imagen": st.column_config.ImageColumn("Imagen de la oferta", help="Previsualización"),
                    "Enlace": st.column_config.LinkColumn("Enlace a la oferta", display_text="Ir a la oferta 🔗"),
                    "Descripción": st.column_config.TextColumn("Descripción / Título", width="large"),
                    "Precio": st.column_config.TextColumn("Precio")
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
                    precio = row['precio_final']

                    # Manejo de nulos (NaN)
                    img_url = img_url if pd.notna(img_url) else "https://via.placeholder.com/300x300?text=Sin+Imagen"
                    enlace = enlace if pd.notna(enlace) else "#"
                    descripcion = descripcion if pd.notna(descripcion) else "Oferta sin descripción"
                    precio_str = f'<p style="color: #e53935; font-size: 28px; font-weight: bold; margin: 10px 0;">{precio}</p>' if pd.notna(precio) else ""

                    with placeholder.container():
                        # Diseño de la tarjeta centrada
                        col1, col2, col3 = st.columns([1, 2, 1])
                        with col2:
                            st.markdown(
                                f"""
                                <div style="text-align: center; padding: 20px; border-radius: 15px; background-color: #f0f2f6; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                                    <img src="{img_url}" style="max-width: 100%; max-height: 400px; border-radius: 10px; object-fit: contain;">
                                    <h2 style="color: #1f77b4; margin-top: 20px;">{descripcion}</h2>
                                    {precio_str}
                                    <a href="{enlace}" target="_blank" style="display: inline-block; background-color: #ff6a00; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 18px; margin-top: 15px;">
                                        ¡Ver Oferta! 🛒
                                    </a>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                    # Pausa según el slider
                    time.sleep(velocidad)

    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
else:
    st.info("Esperando a que subas un archivo CSV para comenzar.")