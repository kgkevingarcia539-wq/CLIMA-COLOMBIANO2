import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta

# ==========================
# CONFIGURACIÓN
# ==========================
st.set_page_config(
    page_title="Clima Pro Colombia",
    page_icon="🌦️",
    layout="centered"
)

# Diccionario de diseños CSS para las tarjetas de clima (Degradados y Emojis Gigantes)
dict_diseno_tarjetas = {
    "☀️ Soleado": {
        "estilo_tarjeta": "background: linear-gradient(135deg, #FFB74D, #F57C00); box-shadow: 0 0 25px rgba(245,124,0,0.5);",
        "emoji_gigante": "☀️",
        "color_fondo_app": "#1a365d"
    },
    "☁️ Nublado": {
        "estilo_tarjeta": "background: linear-gradient(135deg, #B0BEC5, #37474F); box-shadow: 0 0 25px rgba(55,71,79,0.5);",
        "emoji_gigante": "☁️",
        "color_fondo_app": "#2c3e50"
    },
    "🌧️ Lluvioso": {
        "estilo_tarjeta": "background: linear-gradient(135deg, #4FC3F7, #1565C0); box-shadow: 0 0 25px rgba(21,101,192,0.5);",
        "emoji_gigante": "🌧️",
        "color_fondo_app": "#1c2833"
    },
    "⛈️ Tormenta": {
        "estilo_tarjeta": "background: linear-gradient(135deg, #4A148C, #1A237E); box-shadow: 0 0 35px rgba(26,35,126,0.6);",
        "emoji_gigante": "⚡⛈️⚡",
        "color_fondo_app": "#0b0f19"
    },
    "🌤️ Parcialmente nublado": {
        "estilo_tarjeta": "background: linear-gradient(135deg, #90CAF9, #1E88E5); box-shadow: 0 0 25px rgba(30,136,229,0.5);",
        "emoji_gigante": "🌤️",
        "color_fondo_app": "#21618c"
    }
}

# ==========================
# TÍTULO ESTILIZADO
# ==========================
st.markdown('<h1 style="color: white; font-size: 3.2rem; font-weight: 800; margin-bottom: 0px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">🌦️ Clima Pro</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #eaeff2; font-size: 1.1rem; opacity: 0.9; margin-bottom: 25px; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">Reporte meteorológico oficial de Colombia</p>', unsafe_allow_html=True)

# SECTOR INTEGRAL DE TODAS LAS CAPITALES DE COLOMBIA
capitales_colombia = [
    "Seleccione una ciudad de Colombia...", "Arauca", "Armenia", "Barranquilla", "Bogotá D.C.", 
    "Bucaramanga", "Cali", "Cartagena", "Cúcuta", "Florencia", "Ibagué", "Inírida", 
    "Leticia", "Manizales", "Medellín", "Mitú", "Mocoa", "Montería", "Neiva", "Pasto", 
    "Pereira", "Popayán", "Puerto Carreño", "Quibdó", "Riohacha", "San Andrés", 
    "San José del Guaviare", "Santa Marta", "Sincelejo", "Tunja", "Valledupar", "Villavicencio", "Yopal"
]

ciudad = st.selectbox(
    "📍 Elegir el lugar",
    options=capitales_colombia,
    label_visibility="collapsed"
)

if ciudad and ciudad != "Seleccione una ciudad de Colombia...":
    # Lógica aleatoria adaptada térmicamente según regiones lógicas de Colombia
    if ciudad in ["Bogotá D.C.", "Tunja", "Pasto", "Manizales"]:
        temperatura = random.randint(8, 17)  
    elif ciudad in ["Barranquilla", "Cartagena", "Santa Marta", "Riohacha", "Valledupar"]:
        temperatura = random.randint(28, 38) 
    else:
        temperatura = random.randint(18, 29) 

    humedad = random.randint(40, 100)
    viento = round(random.uniform(2, 22), 1)

    estados = ["☀️ Soleado", "☁️ Nublado", "🌧️ Lluvioso", "⛈️ Tormenta", "🌤️ Parcialmente nublado"]
    clima = random.choice(estados)
    cfg = dict_diseno_tarjetas.get(clima)

    # INYECCIÓN DE CSS SEGURO
    estilos_css = f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, {cfg['color_fondo_app']}, #0b0f19);
        background-attachment: fixed;
        transition: background 0.6s ease;
    }}
    div[data-testid="stMetricValue"] {{
        color: #00f2fe !important;
        font-weight: 800 !important;
        font-size: 2.2rem !important;
    }}
    div[data-testid="stMetricLabel"] {{
        color: #ffffff !important;
        font-size: 1rem !important;
    }}
    .glass-box {{
        background: rgba(15, 23, 42, 0.45);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        margin-top: 25px;
        margin-bottom: 25px;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.4);
    }}
    h1, h2, h3, h4, p, span, hr {{
        color: white !important;
    }}
    .clima-card-visual {{
        {cfg['estilo_tarjeta']}
        width: 100%;
        height: 180px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 5rem;
        margin: 15px 0 25px 0;
        border: 1px solid rgba(255,255,255,0.2);
    }}
    .semana-container {{
        display: flex;
        justify-content: space-between;
        background: rgba(0, 0, 0, 0.25);
        border-radius: 12px;
        padding: 12px;
        margin-top: 15px;
    }}
    .dia-item {{ display: flex; flex-direction: column; align-items: center; text-align: center; flex: 1; min-width: 45px; }}
    .dia-item.actual {{ background: rgba(255, 255, 255, 0.1); border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.15); padding: 4px; }}
    .dia-nombre {{ font-size: 0.85rem; font-weight: bold; opacity: 0.8; }}
    .dia-icono {{ font-size: 1.6rem; margin: 4px 0; }}
    .dia-temps {{ font-size: 0.8rem; }}
    .dia-max {{ font-weight: bold; }}
    .dia-min {{ opacity: 0.6; margin-left: 2px; }}
    </style>
    """
    st.markdown(estilos_css, unsafe_allow_html=True)

    # PANEL CONTENEDOR CENTRAL DE CRISTAL
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)

    st.success(f"🇨🇴 Reporte Meteorológico para: {ciudad}")

    st.markdown(f'<div class="clima-card-visual">{cfg["emoji_gigante"]}</div>', unsafe_allow_html=True)

    # Métricas numéricas
    col1, col2, col3 = st.columns(3)
    col1.metric("🌡️ Temperatura", f"{temperatura} °C")
    col2.metric("💧 Humedad", f"{humedad}%")
    col3.metric("🌬️ Viento", f"{viento} km/h")

    # --- MEJORA: GENERACIÓN DE GRÁFICA TOTALMENTE INDEPENDIENTE Y ALEATORIA ---
    st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)
    st.markdown('⚡ **Temperatura** &nbsp;|&nbsp; Precipitaciones &nbsp;|&nbsp; Viento', unsafe_allow_html=True)
    
    horas = ["02:00", "05:00", "08:00", "11:00", "14:00", "17:00", "20:00", "23:00"]
    
    # ¡SOLUCIONADO!: Creamos variaciones horarias dinámicas y únicas usando rangos aleatorios por tramos de día
    temp_madrugada = temperatura + random.randint(-4, -2)
    temp_amanecer = temperatura + random.randint(-6, -4)
    temp_mañana = temperatura + random.randint(-2, 1)
    temp_mediodia = temperatura + random.randint(2, 4)
    temp_tarde = temperatura + random.randint(4, 7)
    temp_atardecer = temperatura + random.randint(1, 3)
    temp_noche = temperatura + random.randint(-2, 0)
    temp_medianoche = temperatura + random.randint(-3, -1)

    temps_horas = [
        temp_madrugada, temp_amanecer, temp_mañana, temp_mediodia, 
        temp_tarde, temp_atardecer, temp_noche, temp_medianoche
    ]
    
    df_horas = pd.DataFrame({"Temperatura (°C)": temps_horas}, index=horas)
    
    # Cambiamos dinámicamente el color de la gráfica horaria según el clima simulado
    color_grafica = "#FF9800" if "Soleado" in clima or "nublado" in clima else "#607D8B"
    st.area_chart(df_horas, color=color_grafica, height=180, use_container_width=True)

    st.markdown('<hr style="border-color: rgba(255,255,255,0.15); margin: 25px 0;">', unsafe_allow_html=True)
    st.markdown(f'<h2 style="font-size: 1.6rem; font-weight: 700; margin-bottom: 10px;">Estado actual: {clima}</h2>', unsafe_allow_html=True)
    st.progress(humedad / 100)

    # BARRA SEMANAL HORIZONTAL
    st.markdown('<div style="margin-top: 25px;"></div>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-size: 1.2rem; font-weight: bold; margin-bottom: 10px;">📅 Pronóstico de 8 días</h3>', unsafe_allow_html=True)

    dias_semana = ["dom", "lun", "mar", "mié", "jue", "vie", "sáb"]
    iconos_simulados = ["☀️", "🌤️", "☁️", "🌧️", "⛈️"]
         
    html_semana = '<div class="semana-container">'
    fecha_base = datetime.now()
    for i in range(8):
        fecha_futura = fecha_base + timedelta(days=i)
        nombre_dia = dias_semana[int(fecha_futura.strftime("%w"))]
        t_max = temperatura + random.randint(-3, 3)
        t_min = t_max - random.randint(5, 10)
        clase_actual = "actual" if i == 0 else ""
        ico_dia = random.choice(["🌧️", "⛈️", "☁️"]) if i >= 4 else random.choice(iconos_simulados)

        html_semana += f'<div class="dia-item {clase_actual}"><div class="dia-nombre">{nombre_dia}</div><div class="dia-icono">{ico_dia}</div><div class="dia-temps"><span class="dia-max">{t_max}°</span><span class="dia-min">{t_min}°</span></div></div>'
    html_semana += '</div>'
    
    st.markdown(html_semana, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
